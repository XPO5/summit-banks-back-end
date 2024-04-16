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
    
def loginCheck(username: str, password: str):
    user_document = {
        "username": username,
        "password": password,
    }
    user = db.find_one_document({"username": username})
    if user == None:
        return None
    if user['password'] == password:
        return user_document
    else:
        return None
    
def transferFunds(from_username: str, to_username: str, amount: float):
    from_user = db.find_one_document({"username": from_username})
    to_user = db.find_one_document({"username": to_username})
    if from_user == None or to_user == None:
        return False
    if from_user['balance'] < amount:
        return False
    
    temp = from_user['balance']
    
    db.update_document(
        {"username": from_username}, 
        {"balance": (from_user['balance'] - amount)}
    )
    db.update_document(
        {"username": to_username}, 
        {"balance": (to_user['balance'] + amount)}
    )
    return True




