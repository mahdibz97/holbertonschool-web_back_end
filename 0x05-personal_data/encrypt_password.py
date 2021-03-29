#!/usr/bin/env python3
""" encrypt """
import bcrypt


def hash_password(password: str) -> bytes:
    """ encrypt """
    p = password.encode()
    return bcrypt.hashpw(p, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ validate """
    return bcrypt.checkpw(password.encode(), hashed_password)
