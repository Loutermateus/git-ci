import json

import requests
from config.headers import Headers
from helper.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from services.users.models.model_list_user import UsersListResponseModel
from services.users.models.model_create_user import CreateUserResponseModel
import allure


class UsersAPI(Helper):



        def __init__(self):
          self.headers = Headers()
          self.endpoints = Endpoints()
          self.payloads = Payloads()


        @allure.step("Get list users ")
        def get_list_all_users(self, offset: int=0, limit: int=10  ) -> UsersListResponseModel:
          response = requests.get(
              url=self.endpoints.list_all_users,
              headers=self.headers.basic,
              params={
                    "offset": offset,
                    "limit": limit
              }
          )
          model = self._validate_response(response, UsersListResponseModel)
          return model

        @allure.step("Delete user by id")
        def delete_user_by_id(self, user_id: str):
            response = requests.delete(
                url=self.endpoints.delete_user_by_id(user_id),
                headers=self.headers.basic
            )
            print(response.status_code)
            print(response.text)  # Или response.json() — если это JSON
            assert response.status_code == 204, f"Failed to delete user with id {user_id}. Status code: {response.status_code}"

        @allure.step("Create user")
        def create_user(self) -> CreateUserResponseModel:
            response = requests.post(
                url=self.endpoints.create_user,
                headers=self.headers.basic,
                json=self.payloads.create_user()
            )
            model = self._validate_response(response, CreateUserResponseModel)
            return model
