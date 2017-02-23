from EVMS import app, db
from project.form import ProjectSetupForm
from project.models import Project
from flask import render_template, redirect, url_for, request, session
from users.models import User
from users.decorators import *

@app.route('/newproject', methods=['POST', 'GET'])
@login_required
def newproject():
    form = ProjectSetupForm()
    
    if request.method == "POST" and form.validate():
        print(session['user_id'])
        user= User.query.filter_by(id= session['user_id']).first()
        project = Project (code= form.code.data, 
                            name= form.name.data, 
                            owner= user.id,
                            description= form.description.data, 
                            start= form.start.data, 
                            finish= form.finish.data, 
                            status= form.status.data)
        db.session.add(project)
        db.session.flush()
        print(project.name + 'Project Name')
        db.session.commit()
        return redirect(url_for('proj_added'))
    return render_template('project/setup.html', form=form, action='new')
    

@app.route('/projectsuccess')
def proj_added():
    return "project added successfully"
    
@app.route('/admin', methods =['GET', 'POST'])
@admin_required
def admin():
    return render_template('project/admin.html')
    
@app.route('/view_projects')
@login_required
def view_projects():
    projects = Project.query.filter_by(status=True).all()
    print (projects)
    return render_template('project/view.html', projects=projects)
    
@app.route('/viewproject/<id>')
@login_required
def project_details(id):
    project = Project.query.filter_by(id= id).first()
    return render_template('project/details.html', project=project)


@app.route('/viewproject/', methods=['POST', 'GET'])
@login_required
def project_detail():
    project_id= request.form['submit']
    session['project_id']= project_id
    project = Project.query.filter_by(id= project_id).first()
    return render_template('project/details.html', project=project)

@app.route('/editproject/<project_id>', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    project = Project.query.filter_by(id= project_id).first()
    form = ProjectSetupForm(obj= project)
    
    if request.method == "POST" and form.validate():
        project.code = form.code.data
        project.start = form.start.data
        project.finish = form.finish.data
        project.status = form.status.data
        project.name = form.name.data
        project.description = form.description.data
        
        db.session.add(project)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('project_details', id= project.id))
    return render_template('project/setup.html', form = form, project=project, action='edit')