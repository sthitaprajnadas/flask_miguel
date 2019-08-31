from base import Session,engine,Base

from base import Session

from blog_app.models import User,Post

session = Session()

user_to_del = session.query(User)\
    .filter(User.username=='admin')\
        .first()
post_to_del = session.query(Post)\
    .filter(Post.id==1).first()

#print ('user to delete is :'+ repr(user_to_del))


session.delete(user_to_del)
#session.delete(post_to_del)
session.commit()
session.close()