import sqlite3

print("START: Task 5 is running")

conn = sqlite3.connect('nyondo_stock.db')
print("Database connected")

def is_valid_name(name):
    result = len(name) >= 2 and '<' not in name and '>' not in name and ';' not in name
    print(f"Checking name '{name}': {result}")
    return result

def is_valid_username(username):
    result = ' ' not in username and len(username) > 0
    print(f"Checking username '{username}': {result}")
    return result

def is_valid_password(password):
    result = len(password) >= 6
    print(f"Checking password length {len(password)}: {result}")
    return result

def search_product_safe(name):
    print(f"Searching for: {name}")
    if not is_valid_name(name):
        print(f"REJECTED: Invalid name '{name}'")
        return []
    query = "SELECT * FROM products WHERE name LIKE ?"
    param = f'%{name}%'
    print(f"Query: {query}, Param: {param}")
    rows = conn.execute(query, (param,)).fetchall()
    print(f"Found {len(rows)} products")
    return rows

def login_safe(username, password):
    print(f"Logging in with: {username} / {password[:2]}***")
    if not is_valid_username(username):
        print(f"REJECTED: Invalid username '{username}'")
        return None
    if not is_valid_password(password):
        print(f"REJECTED: Password too short")
        return None
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    row = conn.execute(query, (username, password)).fetchone()
    print(f"Result: {row}")
    return row

print("=== TASK 5 TEST RESULTS ===")
print()

print("Test 1: search_product_safe('cement')")
result1 = search_product_safe('cement')
print(f"Result: {result1}\n")

print("Test 2: search_product_safe('')")
result2 = search_product_safe('')
print(f"Result: {result2}\n")

print("Test 3: search_product_safe('<script>')")
result3 = search_product_safe('<script>')
print(f"Result: {result3}\n")

print("Test 4: login_safe('admin', 'admin123')")
result4 = login_safe('admin', 'admin123')
print(f"Result: {result4}\n")

print("Test 5: login_safe('admin', 'ab')")
result5 = login_safe('admin', 'ab')
print(f"Result: {result5}\n")

print("Test 6: login_safe('ad min', 'pass123')")
result6 = login_safe('ad min', 'pass123')
print(f"Result: {result6}\n")

conn.close()
print("END: Task 5 complete")
