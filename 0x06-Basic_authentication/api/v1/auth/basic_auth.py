#!/usr/bin/env python3
"""basic auth class template
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """inherits from auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extact a base 64
        """
        if (authorization_header is None) or (not isinstance(
                authorization_header, str)):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
