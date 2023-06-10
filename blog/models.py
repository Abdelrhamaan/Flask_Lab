from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()


class blog_post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer, primary_key=True)
    post_title = db.Column (db.String ,unique=True, nullable=False)
    post_body = db.Column (db.String)
