from services.users.api import UsersAPI



class BaseTest:


     def setup_method(self):
         self.users_api = UsersAPI()
