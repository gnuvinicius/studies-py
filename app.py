from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from applications.controllers.PortalController import PortalController
from applications.services.PortalService import PortalService
from data.repositories.PortalRepository import PortalRepository
from config.flask_app_wrapper import FlaskAppWrapper
from config.routes import Routes

flask_app = Flask(__name__)
# flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@host:port/database_name'
# flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(flask_app)

_repository = PortalRepository()
_service = PortalService(_repository)
_controller = PortalController(_service)

app = FlaskAppWrapper(flask_app)

Routes(app, _controller)


if __name__ == '__main__':
    app.run(debug=True)
