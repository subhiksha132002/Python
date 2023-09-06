# Using Absolute import
# from ecommerce.customer import contact

# Using Relative import
from ..customer import contact

contact.customer_contact()


def calculate_product():
    pass


def calculate_tax():
    pass


print(dir(contact))
