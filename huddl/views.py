import logging

logger = logging.getLogger(__name__)
logger.info('top of views')

from flask import redirect, request, session, url_for, jsonify
from flask.ext.login import login_user, current_user, logout_user, login_required

from sqlalchemy.exc import IntegrityError
from itsdangerous import BadSignature, URLSafeSerializer

from huddl import app, db, login_manager
from helpers import check_auth
from models import User

@app.route('/login/', methods=['POST'])
def login():
    fb_id = request.form['fb_id']
    fb_access_token = request.form['fb_access_token']
    if check_auth(fb_id=fb_id, fb_access_token=fb_access_token):
        user = User.query.filter_by(fb_id=fb_id).first()

        if user is None:
            return jsonify(
                status='error',
                message='could not find user with that fb_id'), 400

        login_user(user, remember=True)
        return jsonify(status='success',
            message='logged in')

@app.route('/logout/', methods=['POST'])
def logout():
    logout_user()
    return jsonify(status='success',
        message='logged out')

@app.route('/register/', methods=['POST'])
def register():
    user_data = {k:request.form[k] for k in (
        'name','fb_id','fb_access_token')}
    user = User(**user_data)
    if check_auth(user=user):
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            return jsonify(
                status='error',
                message="that user already exists!"), 400
        login_user(user, remember=True)
        return jsonify(status='success',
            message='registered')
    else:
        return jsonify(
            status='error',
            message='authentication failed'), 400

@app.route('/whoami/')
@login_required
def whoami():
    return jsonify(
        name=current_user.name,
        fb_id=current_user.fb_id,
        phone=current_user.phone,
        email=current_user.email)

@login_manager.unauthorized_handler
def unauthorized_access():
    return jsonify(
        status='error',
        message="you're not authorized to do that! (try loggin in)"), 401
