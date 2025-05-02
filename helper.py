import faker
from faker import Faker

faker = Faker()

def generate_registration_data(length=None):
    name = faker.name()
    if length is None or length <= 2:
        length = 5
    email = faker.email()
    if length is None or length <= 5:
        length = 8
    password = faker.password(
        length=length,
        digits=True,
        upper_case=True,
        lower_case=True
    )
    return name, email, password