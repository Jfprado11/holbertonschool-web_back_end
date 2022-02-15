#!/usr/bin/env python3
"""basic auth class template
"""

import binascii
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """inherits from auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extact a base 64
        """
        if (authorization_header is None) or (not isinstance(
                authorization_header, str)):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode a base 64 auth header
        """
        if (base64_authorization_header is None) or (not isinstance(
                base64_authorization_header, str)):
            return None
        try:
            decodi = base64.b64decode(base64_authorization_header)
            return decodi.decode("utf-8")
        except binascii.Error:
            return None
