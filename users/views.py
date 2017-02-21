from EVMS import app, db
from flask import render_template, redirect, session, request, url_for
from users.form import RegisterForm, LoginForm
from users.models import User
from users.decorators import login_required
from project.models import Project
import bcrypt


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        author = User.query.filter_by(
            username=form.username.data,
            ).first()
        if author:
            if bcrypt.hashpw(form.password.data, author.password) == author.password:
                session['username'] = form.username.data
                session['is_admin'] = author.is_admin
                session['user_id'] = author.id
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('login_success'))
            else:
                error = "Incorrect password"
        else:
            error = "User not found"
    return render_template('users/login.html', form=form, error=error)

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
        
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)  
        user= User(form.firstname.data,
                    form.lastname.data, 
                    form.email.data, 
                    form.username.data, 
                    hashed_password)
        
        db.session.add(user)
        db.session.commit()
        return redirect('/success')
    return render_template('users/register.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))


@app.route('/success')
def success():
    return "User registered!"
@app.route('/')
@app.route('/login_success')
@login_required
def login_success():
    projects = Project.query.all()
    return render_template('/project/projectselection.html', projects= projects)