import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash

from rpg.db import get_db, select_user, insert_user

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif select_user(username) is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            if insert_user(username, password):
                return redirect(url_for('auth.login'))
            error = 'Error in inserting user to database'

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    username = select_user("teste")["username"]
    return render_template('auth/login.html', username=username)