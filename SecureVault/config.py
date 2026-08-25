"""
Project configuration.

This file stores application-wide constants so they can be changed
from one place instead of searching through the codebase.
"""

from pathlib import Path

# -------------------------------------------------------------------
# Project Paths
# -------------------------------------------------------------------

# Root folder of the project
BASE_DIR = Path(__file__).resolve().parent

# Folder where encrypted vault will be stored
VAULT_DIR = BASE_DIR / "vault"

# Encrypted vault file
VAULT_FILE = VAULT_DIR / "vault.enc"

# Salt file
SALT_FILE = VAULT_DIR / "salt.bin"

MASTER_HASH_FILE = VAULT_DIR / "master.hash"

SECRET_KEY = "change-this-to-a-random-secret-key"

# -------------------------------------------------------------------
# Application Info
# -------------------------------------------------------------------

APP_NAME = "SecureVault"

VERSION = "1.0.0"