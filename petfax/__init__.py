# import Flask (to use like express in node) and other dependencies:
from flask import Flask 
from flask_migrate import Migrate


# factory
def create_app(): 
    app = Flask(__name__)

    # database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ruckus179@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)


    # initial route
    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app
    return app





