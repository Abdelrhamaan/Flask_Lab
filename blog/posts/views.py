from blog.models import blog_post, db
from flask import render_template, request, redirect ,url_for
from blog.posts.myBlueprints import posts_blueprint


@posts_blueprint.route('postlist' , endpoint='post_list')


def post_list ():
    all_posts = blog_post.query.all()

    return render_template('post_list.html',all_posts=all_posts)

@posts_blueprint.route('postlist/<int:id>' , endpoint='post_show')

def post_show(id):

    post = blog_post.query.get_or_404(id)
    return render_template('post_view.html',post=post)

@posts_blueprint.route('createpost' ,methods=['GET','POST'], endpoint='post_create')
def post_create ():
    if request.method =='POST':
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

@posts_blueprint.route('postdelete/<int:id>' ,endpoint='post_delete')
def post_delete (id):
    del_post= blog_post.query.get_or_404(id)
    db.session.delete(del_post)
    db.session.commit()
    return redirect(url_for('posts.post_list'))



