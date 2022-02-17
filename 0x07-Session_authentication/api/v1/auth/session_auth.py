#!/usr/bin/env python3
"""making a session auth class
"""

import uuid
from api.v1.auth.auth import Auth
from models.user import User


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

    def current_user(self, request=None):
        """based on cookie value
        """
        cookie_value = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_value)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """destroys the session
        """
        if request is None:
            return False

        cookie = self.session_cookie(request)
        if cookie is None:
            return False

        user_id = self.user_id_for_session_id(cookie)
        if user_id is None:
            return False

        del self.user_id_by_session_id[cookie]
        return True
