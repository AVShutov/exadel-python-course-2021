def create_user(*user, age=42, **extra):
    return {
        'name': user[0],
        'surname': user[1],
        'age': age,
        'extra': extra
    }

assert create_user("John", "Doe") == \
        {
            "name": "John",
            "surname": "Doe",
            "age": 42,
            "extra": {}
        }

assert create_user("Bill", "Gates", age=65) == \
        {
            "name": "Bill",
            "surname": "Gates",
            "age": 65,
            "extra": {}
        }

assert create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True) == \
        {
            "name": "Marie",
            "surname": "Curie",
            "age": 66,
            "extra": {
                "occupation": "physicist",
                "won_nobel": True
            }
        }