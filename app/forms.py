from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired,Email,Length, Regexp, Required
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name= StringField('Last Name', validators=[InputRequired()])
    gender=SelectField('Gender',choices= [('F','Female'), ('M','Male')], default = 'F')
    email=StringField('Email', validators=[Email()], render_kw={'placeholder' :'e.g. someemail@example.com'})
    location=StringField('Location', validators=[InputRequired()], render_kw={'placeholder' : 'e.g. Kingston,Jamaica'})
    bio=TextAreaField('Biography', validators=[InputRequired(),Length(max=200)])
    photo= FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only')])

