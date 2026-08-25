"""
Encryption service using AES-GCM.
"""

import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt(data: bytes, key: bytes) -> bytes:
    """
    Encrypt data using AES-GCM.

    Parameters
    ----------
    data : bytes
        Plaintext bytes.

    key : bytes
        32-byte encryption key.

    Returns
    -------
    bytes
        Nonce + Ciphertext.
    """

    aes = AESGCM(key)

    nonce = os.urandom(12)

    ciphertext = aes.encrypt(nonce, data, None)

    return nonce + ciphertext


def decrypt(encrypted_data: bytes, key: bytes) -> bytes:
    """
    Decrypt AES-GCM encrypted data.

    Parameters
    ----------
    encrypted_data : bytes
        Stored encrypted data (nonce + ciphertext).

    key : bytes
        Encryption key.

    Returns
    -------
    bytes
        Original plaintext.
    """

    aes = AESGCM(key)

    nonce = encrypted_data[:12]

    ciphertext = encrypted_data[12:]

    return aes.decrypt(nonce, ciphertext, None)