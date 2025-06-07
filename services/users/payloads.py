from faker import Faker

faker = Faker()

class Payloads:



     def create_user(self):
           return {
                "email": faker.email(),
                "password": faker.password(),
                "name": faker.name(),
                "nickname": faker.user_name()
           }


print(Payloads().create_user())