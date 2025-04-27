import faker
from faker import Faker

faker = Faker()

def generate_registration_data(length=None):
    email = faker.email()
    if length is None or length <= 5:
        length = 8
    password = faker.password(
        length=length,
        digits=True,
        upper_case=True,
        lower_case=True
    )
    return email, password