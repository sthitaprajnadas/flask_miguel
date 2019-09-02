from blog_app import app_var
from flask import render_template,redirect,flash,url_for,request
from blog_app.forms import LoginForm
from blog_app.models import User
from blog_app.forms import LoginForm
from flask_login import current_user,login_user,logout_user,login_required
from werkzeug.urls import url_parse


@app_var.route('/')
@app_var.route('/index')
@login_required
def index():
    user = { 'username' : 'Miguel','age':28 }
    posts = [{'authorname':'Dan Brown' , 'content':'Da vinci Code is beautiful!'},
    {'authorname':'Sir Conan Doyle' , 'content':'Sherlock Holmes is a freak!'}]
    return render_template('index.html',title='Home',user=user, posts=posts)

@app_var.route('/login',methods=['GET','POST'])
def signin():
    if current_user.is_authenticated:
         return redirect(url_for('index'))
    
    form = LoginForm()

    #for post request
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or user.check_password(form.password.data):
            flash("incorrect username and password!")
            return redirect(url_for('signin'))

        login_user(user,remember=form.rememberMe.data)

        flash('logged in as : {}, with remember me {}'.format(form.username.data,form.rememberMe.data))
        
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '' or next_page == '/':
            next_page=url_for('index')
        
        return redirect(url_for(next_page))


    return render_template('login.html',title='Sign In',form=form)

app_var.route('/logout')
def signout():
    logout_user()
    return redirect(url_for('index'))
