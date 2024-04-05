from src.utils.database import Database

db = Database()

def addUserIfNotExists(username: str, password: str, email: str, first_name: str, last_name: str, initial_balance: float):
    user_document = {
        "username": username,
        "password": password,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "balance": initial_balance,
    }
    username_exists = db.find_one_document({"username": username})
    email_exists = db.find_one_document({"email": email})

    if username_exists == None and email_exists == None:
        db.insert_document(user_document)
        return user_document
    else:
        return None