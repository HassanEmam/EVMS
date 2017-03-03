from functools import wraps
from flask import session, request, redirect, url_for, abort

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login', next=request.url))
        elif session.get('is_admin') is None:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function
    
def project_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('project_id') is None:
            return redirect(url_for('login_success', next=request.url))
        return f(*args, **kwargs)
    return decorated_function