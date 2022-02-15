#!/usr/bin/env python3
"""
handling the auth with a class
"""

from typing import List, TypeVar
from flask import request


class Auth():
    """a class to check the basic auth to the paths
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """wether the path needs auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """check if the header recive the auth
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns the current log user
        """
        return None
