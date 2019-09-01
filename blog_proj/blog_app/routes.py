from blog_app import app_var
from flask import render_template,redirect,flash,url_for
from blog_app.forms import LoginForm


@app_var.route('/')
@app_var.route('/index')
def index():
    user = { 'username' : 'Miguel','age':28 }
    posts = [{'authorname':'Dan Brown' , 'content':'Da vinci Code is beautiful!'},
    {'authorname':'Sir Conan Doyle' , 'content':'Sherlock Holmes is a freak!'}]
    return render_template('index.html',title='Home',user=user, posts=posts)

@app_var.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    #for post request
    if form.validate_on_submit():
        flash('logged in as : {}, with remember me {}'.format(form.username.data,form.rememberMe.data))
        return redirect(url_for('index'))


    return render_template('login.html',title='Sign In',form=form)
