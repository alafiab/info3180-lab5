"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, models, forms
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import current_user
from models import UserProfile
from datetime import datetime, date
from flask import send_from_directory
from forms import UserForm
from werkzeug.utils import secure_filename
import os


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/profile', methods=['POST','GET'])
def profile():
    form = UserForm()
    user= None
    if request.method =='POST' and form.validate_on_submit():
        first_name,last_name,gender,email,location,bio,photo = [form.first_name.data,form.last_name.data,form.gender.data,form.created_on.data,form.email.data,form.location.data,form.bio.data,form.photo.data]
        if not UserProfile.query.filter_by(email=email).first():
            if gender == 'F':
                gender = "FEMALE"
            else:
                gender = "MALE"
            
            filename= secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            user = UserProfile(first_name = first_name, last_name = last_name, 
                gender = gender, created_on= created_on,bio = bio, photo = filename, location = location, email = email)
            
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('profiles'))
        else:
            flash('This email is already linked to a profile.', 'danger')
            return render_template('forms.html', form = form)
        
    return render_template('forms.html',form=form)
    
@app.route('/profiles')
def profiles():
    users = UserProfile.query.all()
    print(users)
    return render_template('profiles.html', users = users)
    
@app.route('/profiles/<userid>')  
def show_profile(userid):
    if userid:
        user =UserProfile.query.filter_by(id=userid).first()
        photo= get_uploaded_images()
        print user
    return render_template('profile.html',user=user,photo=photo,created_on = format_date_joined())
    
def get_uploaded_images():
    rootdir = os.getcwd()
    print rootdir
    ls =[]
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
            ls.append(os.path.join(subdir, file).split('/')[-1])
    return ls
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    
def format_date_joined():
    created_on = date(2018, 3, 12)
    return created_on.strftime("%B %e, %Y")



def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
