from py42.services import BaseService


class AdministrationService(BaseService):
    def get_current_tenant(self):
        uri = "/c42api/v3/customer/my"
        return self._connection.get(uri)
