def login(username, password):
    return username == "admin" and password == "1234"

print("Login Module")
print("Login successful:", login("admin", "1234"))