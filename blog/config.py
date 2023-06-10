


class Config:
    @staticmethod
    def init_app():
        pass





class dev_config(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
class prod_config(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:leomessi4ever@localhost:5432/blog"


proj_config = {
    'dev' : dev_config ,
    'prod' : prod_config
}