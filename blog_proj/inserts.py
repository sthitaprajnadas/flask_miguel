from base import Session,engine,Base

from blog_app.models import User,Post

Base.metadata.create_all(engine)

session = Session()

admin_user = User('admin','admin@gmail.com',hash('default'))

first_post = Post(body='My First Post Body',user_id=1,title='My first Post title')

session.add(admin_user)
session.add(first_post)


session.commit()
session.close()