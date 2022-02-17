#!/usr/bin/env python3
"""making a session auth class
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """class to new auth session
    """

    def __init__(self) -> None:
        super().__init__()
