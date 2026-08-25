"""
Vault Service (Secure Version)

Responsibilities:
- Create vault
- Load vault
- Save vault (AES encrypted)
- CRUD operations
- Search
"""

import json
from config import VAULT_FILE
from services.encryption import encrypt, decrypt


class VaultService:

    def __init__(self, key: bytes):
        self.key = key

        self.vault = {
            "accounts": []
        }

    # --------------------------------------------------------
    # CREATE VAULT
    # --------------------------------------------------------

    def create_empty_vault(self):
        """Create an empty encrypted vault (first time only)."""

        self.vault = {"accounts": []}
        self.save()

    # --------------------------------------------------------
    # SAVE VAULT (ENCRYPTED)
    # --------------------------------------------------------

    def save(self):
        """Encrypt and save vault to disk."""

        plaintext = json.dumps(self.vault).encode()

        encrypted = encrypt(plaintext, self.key)

        with open(VAULT_FILE, "wb") as f:
            f.write(encrypted)

    # --------------------------------------------------------
    # LOAD VAULT (DECRYPTED)
    # --------------------------------------------------------

    def load(self):
        """Load and decrypt vault from disk."""

        with open(VAULT_FILE, "rb") as f:
            encrypted = f.read()

        plaintext = decrypt(encrypted, self.key)

        self.vault = json.loads(plaintext.decode())

    # --------------------------------------------------------
    # ADD ACCOUNT (ENCRYPT PASSWORD FIELD)
    # --------------------------------------------------------

    def add_account(self, website: str, username: str, password: str):

        encrypted_password = encrypt(
            password.encode(),
            self.key
        ).hex()

        self.vault["accounts"].append({
            "website": website,
            "username": username,
            "password": encrypted_password
        })

        self.save()

    # --------------------------------------------------------
    # GET ACCOUNTS (DECRYPT PASSWORDS)
    # --------------------------------------------------------

    def get_accounts(self):

        accounts = []

        for acc in self.vault["accounts"]:

            try:
                decrypted_password = decrypt(
                    bytes.fromhex(acc["password"]),
                    self.key
                ).decode()

            except Exception:
                decrypted_password = "ERROR"

            accounts.append({
                "website": acc["website"],
                "username": acc["username"],
                "password": decrypted_password
            })

        return accounts

    # --------------------------------------------------------
    # DELETE ACCOUNT
    # --------------------------------------------------------

    def delete_account(self, website: str):

        self.vault["accounts"] = [
            acc for acc in self.vault["accounts"]
            if acc["website"].lower() != website.lower()
        ]

        self.save()

    # --------------------------------------------------------
    # UPDATE ACCOUNT
    # --------------------------------------------------------

    def update_account(self, website: str, username: str, password: str):

        for acc in self.vault["accounts"]:

            if acc["website"].lower() == website.lower():

                acc["username"] = username

                acc["password"] = encrypt(
                    password.encode(),
                    self.key
                ).hex()

        self.save()

    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    def search(self, keyword: str):

        keyword = keyword.lower()

        return [
            acc for acc in self.get_accounts()
            if keyword in acc["website"].lower()
        ]