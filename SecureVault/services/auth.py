"""
Authentication & Key Derivation Module
"""

import os

from argon2 import PasswordHasher
from argon2.low_level import hash_secret_raw, Type
from argon2.exceptions import VerifyMismatchError

from config import SALT_FILE, MASTER_HASH_FILE

ph = PasswordHasher()


# ---------------- SALT ----------------

def generate_salt(length: int = 16) -> bytes:
    return os.urandom(length)


def save_salt(salt: bytes) -> None:
    SALT_FILE.parent.mkdir(exist_ok=True)
    with open(SALT_FILE, "wb") as file:
        file.write(salt)


def load_salt() -> bytes:
    with open(SALT_FILE, "rb") as file:
        return file.read()


# ---------------- KEY DERIVATION ----------------

def derive_key(master_password: str, salt: bytes) -> bytes:
    return hash_secret_raw(
        secret=master_password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32,
        type=Type.ID
    )


# ---------------- MASTER PASSWORD ----------------

def save_master_password(master_password: str):
    """
    Hash and store master password
    """

    MASTER_HASH_FILE.parent.mkdir(parents=True, exist_ok=True)

    password_hash = ph.hash(master_password)

    with open(MASTER_HASH_FILE, "w") as file:
        file.write(password_hash)


def verify_master_password(master_password: str) -> bool:
    """
    Verify master password safely
    """

    try:
        with open(MASTER_HASH_FILE, "r") as file:
            stored_hash = file.read()

        return ph.verify(stored_hash, master_password)

    except (VerifyMismatchError, FileNotFoundError):
        return False