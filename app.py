from flask import Flask, url_for
from flask import render_template ,request ,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

## creating the app
app = Flask(__name__)


## connect to db


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db=SQLAlchemy(app)

##------view posts ------------->>>
@app.route('/viewpost/<int:id>' ,endpoint='post_view')
def post_show(id):

    post = blog_post.query.get_or_404(id)
    return render_template('post_view.html',post=post)


##-----------------Create Posts------------->>>
@app.route('/createpost' , methods=['GET','POST'] ,endpoint='post_create')
def post_create ():
    if request.method =='POST' :
        post_title = request.form['post_name']
        post_body =  request.form['post_body']
        # image = request.files['image']
        # filename = secure_filename(image.filename)
        # image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        created_post = blog_post (post_title = post_title , post_body =post_body  ) ##,image_filename=filename

        db.session.add(created_post)
        db.session.commit()

        return redirect('/postlist')
    return render_template('create_post.html')

## ----------------All Posts List ----------->>>>
@app.route('/postlist' ,endpoint='post_list')
def post_list ():
    myPosts = blog_post.query.all()

    return render_template('post_list.html',myPosts=myPosts)
# app.add_url_rule('/postlist',view_func=post_list)


##---------------- delte Post ---------------->>>>.
@app.route('/postdelete/<int:id>' ,endpoint='post_delete')
def post_delete (id):
    del_post= blog_post.query.get_or_404(id)
    db.session.delete(del_post)
    db.session.commit()
    return redirect(url_for('post_list'))












#-----------------Posts Model -------------------->>

class blog_post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer, primary_key=True)
    post_title = db.Column (db.String ,unique=True, nullable=False)
    post_body = db.Column (db.String)
    # image_filename = db.Column(db.String(100), nullable=True)
