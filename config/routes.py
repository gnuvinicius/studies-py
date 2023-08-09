from applications.controllers import PortalController
from config.flask_app_wrapper import FlaskAppWrapper


class Routes:

    def __init__(self, app: FlaskAppWrapper, controller: PortalController) -> None:
        self.app = app
        self._controller = controller
        self.define_routes()

    def define_routes(self):
        self.app.add_endpoint('/action', 'action',
                              self._controller.get_all_order, methods=['GET'])
