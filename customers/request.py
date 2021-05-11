CUSTOMERS = [
    {
        "email": "cb@gmail.com",
        "password": "cb",
        "name": "chuck Butters",
        "id": 1
    },
    {
        "email": "t@gmail.com",
        "password": "cam",
        "name": "Tyler tyler",
        "id": 2
    },
    {
        "email": "cv@df",
        "password": "dfdf",
        "name": "cb cv",
        "id": 3
    }

def get_all_locations():
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found location, if it exists
    requested_customer = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
