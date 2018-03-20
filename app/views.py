"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, models, forms
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
from models import UserProfile
from datetime import datetime, date
from forms import UserForm
from werkzeug.utils import secure_filename
import os


###
# Routing for your application.
###

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/profile', methods=['POST','GET'])
@app.route('/profile/<userid>', methods= ['GET'])
def profile(userid = None):
    form = UserForm()
    user= None
    if request.method =='POST' and form.validate_on_submit():
        first_name,last_name,gender,email,location,bio,photo = [form.first_name.data,form.last_name.data,form.gender.data,form.email.data,form.location.data,form.bio.data,form.photo.data]
        if UserProfile.query.filter_by(email=email).first():
            filename= secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            user = UserProfile(first_name = first_name, last_name = last_name, gender = gender, email = email, location = location, bio = bio)
            db.session.add(user)
            db.session.commit()
        filename= secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return redirect(url_for('profiles'))
    if(userid):
        return userid
    return render_template('forms.html',form=form)
    
@app.route('/profiles')
def profiles():
    users = UserProfile.query.all()
    print(users)
    return render_template('profiles.html', users = users)
    



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
