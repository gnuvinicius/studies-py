from flask import jsonify, request
from applications.services.PortalService import PortalService
from models.order import Order


class PortalController:

    def __init__(self, service: PortalService):
        self._service = service

    def get_all_order(self):
        result = []
        for oc in self._service.get_all():
            result.append(oc)

        return jsonify(result)

    def change_title(self) -> list[Order]:
        id = request.args.get('id')
        title = request.args.get('title')
        try:
            result = []
            for oc in self._service.change_title(id, title):
                result.append(oc.__dict__)

            return jsonify(result)
        except Exception as e:
            return jsonify(str(e)), 400
