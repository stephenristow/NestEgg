from django.db import connection
import mysql.connector
import os


def create_connection():
    connection = mysql.connector.connect(
        host = '',
        user = '',
        password = '',
        database = ''
    )
    return connection

def add_account():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO Account(email, account_name, account_type) VALUES (%s, %s, %s)
        """
        cursor.execute(query, (email, account_name, account_type,))
        connection.commit()
        return True
    except Exception as e:
        return False 
    finally:
        cursor.close()
        connection.close()

def get_account(email, account_name, account_type):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        SELECT * FROM Account WHERE email = %s AND account = %s AND account_type = %s
"""
        cursor.execute(query, (email, account_name,account_type,))
        account = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return balance
    except Exception as e:
        return None

def get_transactions(email, account_name, account_type):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        SELECT transaction_type, amount, transaction_time FROM Account WHERE email = %s AND account = %s AND account_type = %s
"""
        cursor.execute(query, (email, account_name,account_type,))
        transactions = cursor.fetchall()
        cursor.close()
        connection.close()
        return transactions
    except Exception as e:
        return None


def add_withdraw(email, account_name, account_type, amount):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        bal_query = """
        UPDATE Account SET balance = balance - %s WHERE email = %s AND account_name = %s AND account_type = %s
"""
        with_query = """
        INSERT INTO Transactions (email, account_name, account_type, transaction_type, amount) VALUES (%s, %s, %s, 'Withdrawal', %s)
"""
        cursor.start_transaction()
        cursor.execute(bal_query, (amount, email, account_name, account_type,))
        cursor.execute(with_query, (email, account_name, account_type, amount,))
        connection.commit()
        return True
    except Exception as e:
        cursor.rollback()
        return False
    finally:
        cursor.close()
        connection.close()


def add_deposit(email, account_name, account_type, amount):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        bal_query = """
        UPDATE Account SET balance = balance + %s WHERE email = %s AND account_name = %s AND account_type = %s
"""
        dep_query = """
        INSERT INTO Transactions (email, account_name, account_type, transaction_type, amount) VALUES (%s, %s, %s, 'Deposit', %s)
"""
        cursor.start_transaction()
        cursor.execute(bal_query, (amount, email, account_name, account_type,))
        cursor.execute(dep_query, (email, account_name, account_type, amount,))

        connection.commit()
        return True
    except Exception as e:
        cursor.rollback()
        return False
    finally:
        cursor.close()
        connection.close()

def add_transfer(email, account_name1, account_type1, account_name2, account_type2, amount):
    # money is moving from account1 to account2
    try:
        connection = create_connection()
        cursor = connection.cursor()
        bal_query1 = """
        UPDATE Account SET balance = balance - %s WHERE email = %s AND account_name = %s AND account_type = %s
"""
        bal_query2 = """
        UPDATE Account SET balance = balance + %s WHERE email = %s AND account_name = %s AND account_type = %s
"""
        with_query = """
        INSERT INTO Transactions (email, account_name, account_type, transaction_type, amount) VALUES (%s, %s, %s, 'Withdrawal', %s)
"""
        dep_query = """
        INSERT INTO Transactions (email, account_name, account_type, transaction_type, amount) VALUES (%s, %s, %s, 'Deposit', %s)
"""
        cursor.start_transaction()
        cursor.execute(bal_query1, (amount, email, account_name1, account_type1,))
        cursor.execute(bal_query1, (amount, email, account_name2, account_type2,))
        cursor.execute(with_query, (amount, email, account_name1, account_type1,))
        cursor.execute(dep_query, (amount, email, account_name2, account_type2,))

        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        return False
    finally:
        cursor.close()
        connection.close()

def calculate_interest(email, account_name, account_type):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        SELECT balance, interest FROM BankAccount WHERE email = %s AND account_name = %s AND account_type = %s
"""
        cursor.execute(query, (email, account_name, account_type,))
        balance, interest = cursor.fetchone()[0], cursor.fetchone()[1]
        cursor.close()
        connection.close()
        total_interest = balance * interest / 100
        return total_interest
    except Exception as e:
        return False
    
def calculate_earnings():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = """
         
"""

    except Exception as e:
        return None
