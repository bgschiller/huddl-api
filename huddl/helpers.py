import logging

from functools import wraps

from flask import session

logger = logging.getLogger(__name__)

def check_auth(**kwargs):
    assert any((
        ('fb_id' in kwargs and 'fb_access_token' in kwargs),
        ('user' in kwargs)))
    return True
