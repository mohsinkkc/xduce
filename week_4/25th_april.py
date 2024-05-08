'''
ACID PROPERITIES : 

Atomicity : ALll changes to data must be perform successfully or not at all

Consistence : Data must be consistent before and after transcation

Isolated :No other can change the data while the transcation is running

Durable:The change made by transcation must be persist/Not changeable unless or until updated

'''
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="XDuce@123",
    database="person"
)
cursor = conn.cursor()

# Create a table for demonstration
cursor.execute("CREATE TABLE IF NOT EXISTS transactions (id INT AUTO_INCREMENT PRIMARY KEY, amount DECIMAL(10, 2))")

def insert_transaction(amount):
    # Insert a transaction into the table
    sql = "INSERT INTO transactions (amount) VALUES (%s)"
    cursor.execute(sql, (amount,))
    conn.commit()
    print("Transaction inserted successfully.")

def read_transactions():
    # Read all transactions from the table
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    print("All Transactions:")
    for transaction in transactions:
        print(transaction)

def update_transaction(transaction_id, new_amount):
    # Update a transaction
    sql = "UPDATE transactions SET amount = %s WHERE id = %s"
    cursor.execute(sql, (new_amount, transaction_id))
    conn.commit()
    print("Transaction updated successfully.")

def delete_transaction(transaction_id):
    # Delete a transaction
    sql = "DELETE FROM transactions WHERE id = %s"
    cursor.execute(sql, (transaction_id,))
    conn.commit()
    print("Transaction deleted successfully.")

try:
    # Perform transactions
    amount=input("enter the amount :")
    insert_transaction(amount)
    read_transactions()
    id=input("enter the id :")
    update_amount=int(input("enter amount to be updated:"))
    update_transaction(id, update_amount)
    delete_item=int(input("enter the id to delete :"))
    delete_transaction(delete_item)
    read_transactions()

except Exception as e:
    print("Error:", e)

finally:
    # Close the database connection
    cursor.close()
    conn.close()
