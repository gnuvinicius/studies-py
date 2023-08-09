from data.repositories.PortalRepository import PortalRepository
from models.order import Order


class PortalService:

    def __init__(self, repository: PortalRepository):
        self._repository = repository

        self.list: list[Order] = []

        # self.list.append(Order(10105, 'buy a black bike', 19.659))
        # self.list.append(Order(10106, 'buy a earphone', 150.9))
        # self.list.append(Order(10107, 'testing web api', 20.01))

    def get_all(self) -> list[Order]:
        return self._repository.get_all()

    def change_title(self, id: str, title: str) -> list[Order]:
        try:
            for order in self.list:
                if order.id == id:
                    order.title = title

            return self.list
        except Exception as e:
            raise ValueError(e)
