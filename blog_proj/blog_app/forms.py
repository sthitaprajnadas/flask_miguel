from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username=StringField('Usrename',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    rememberMe=BooleanField('Remember me')
    submit=SubmitField('Sign In')
    
