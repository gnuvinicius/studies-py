from flask import Flask

from applications.controllers import PortalController


class FlaskAppWrapper:

    def __init__(self, app: Flask, **configs):
        self.app = app
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name,
                              handler, methods=methods, *args, **kwargs)

    def run(self, **kwargs):
        self.app.run(**kwargs)

    # @app.route("/get-all")
    # def get_all(self):
    #     return self._controller.get_all_order()

    # @app.route('/change-title', methods=['GET'])
    # def change_title(self):
    #     return self._controller.change_title()
