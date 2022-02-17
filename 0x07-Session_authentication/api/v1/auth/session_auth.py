#!/usr/bin/env python3
"""making a session auth class
"""

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """class to new auth session
    """

    user_id_by_session_id = {}

    def __init__(self) -> None:
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """creates the session id
        """
        if (user_id is None) or (not isinstance(user_id, str)):
            return None

        new_id = str(uuid.uuid4())
        self.user_id_by_session_id[new_id] = user_id
        return new_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns teh user id bases on the session
        """
        if (session_id is None) or (not isinstance(session_id, str)):
            return None

        user = self.user_id_by_session_id.get(session_id)
        return user