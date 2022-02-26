#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

import requests


def register_user(email: str, password: str) -> None:
    """register a user"""
    form_data = {"email": email, "password": password}
    resp = requests.post('http://127.0.0.1:5000/users', data=form_data)
    assert resp.status_code == 200
    assert resp.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """log the wrong password
    """
    form_data = {"email": email, "password": password}
    resp = requests.post('http://127.0.0.1:5000/sessions', data=form_data)
    assert resp.status_code == 401


def log_in(email: str, password: str) -> str:
    """log in to the session
    """
    form_data = {"email": email, "password": password}
    resp = requests.post('http://127.0.0.1:5000/sessions', data=form_data)
    assert resp.status_code == 200
    assert resp.json() == {"email": email, "message": "logged in"}
    return resp.cookies["session_id"]


def profile_unlogged() -> None:
    """profile not log
    """
    resp = requests.get('http://127.0.0.1:5000/profile')
    assert resp.status_code == 403


def profile_logged(session_id: str) -> None:
    """progfile log
    """
    form_data = {"session_id": session_id}
    resp = requests.get('http://127.0.0.1:5000/profile', cookies=form_data)
    assert resp.status_code == 200
    assert resp.json() == {"email": resp.json()["email"]}


def log_out(session_id: str) -> None:
    """loggin out
    """
    form_data = {"session_id": session_id}
    resp = requests.delete('http://127.0.0.1:5000/sessions', data=form_data)
    resp.status_code == 200


def reset_password_token(email: str) -> str:
    """reset the poassweord
    """
    form_data = {"email": email}
    resp = requests.post(
        'http://127.0.0.1:5000/reset_password', data=form_data)
    assert resp.status_code == 200
    assert resp.json() == {"email": resp.json()[
        "email"], "reset_token": resp.json()["reset_token"]}
    return resp.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """updating the password
    """
    form_data = {"email": email, "reset_token": reset_token,
                 "new_password": new_password}
    resp = requests.put(
        'http://127.0.0.1:5000/reset_password', data=form_data)
    assert resp.status_code == 200
    assert resp.json() == {"email": resp.json()["email"],
                           "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
