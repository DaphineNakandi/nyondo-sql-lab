import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# A - all columns all products
print("A:")
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows: print(r)

# B - only name and price
print("\nB:")
rows = conn.execute('SELECT name, price FROM products').fetchall()
for r in rows: print(r)

# C - product with id = 3
print("\nC:")
row = conn.execute('SELECT * FROM products WHERE id = 3').fetchone()
print(row)

# D - name contains 'sheet'
print("\nD:")
rows = conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall()
for r in rows: print(r)

# E - sorted by price highest first
print("\nE:")
rows = conn.execute('SELECT * FROM products ORDER BY price DESC').fetchall()
for r in rows: print(r)

# F - two most expensive
print("\nF:")
rows = conn.execute('SELECT * FROM products ORDER BY price DESC LIMIT 2').fetchall()
for r in rows: print(r)

# G - update cement price to 38000
conn.execute('UPDATE products SET price = 38000 WHERE id = 1')
conn.commit()
print("\nG:")
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows: print(r)

conn.close()