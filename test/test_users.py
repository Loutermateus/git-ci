import pytest
import allure

from config.base_test import BaseTest

@allure.epic("Test User")
class TestUsers(BaseTest):

    @pytest.mark.smoke
    @allure.title("Find and delete user")
    def test_users(self):
        # user = self.users_api.create_user()
        # self.users_api.delete_user_by_id(user.uuid)
        self.users_api.get_list_all_users()
        self.users_api.delete_user_by_id("afb293ae-04d3-4442-8913-6a643b5878ad")

    @pytest.mark.smoke
    @allure.title("Delete user")
    def test_user_0(self):
        user = self.users_api.create_user()
        self.users_api.delete_user_by_id(user.uuid)

    @pytest.mark.smoke
    @allure.title("Get list user")
    def test_user_1(self):
        self.users_api.get_list_all_users()


    @pytest.mark.user
    @allure.title("Get list user")
    def test_user_2(self):
        self.users_api.get_list_all_users()

    @pytest.mark.user
    @allure.title("Get list user")
    def test_user_3(self):
        self.users_api.get_list_all_users()
