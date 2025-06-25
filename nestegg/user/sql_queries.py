from django.db import connection
import mysql.connector
import os

from argon2 import PasswordHasher

ph = PasswordHasher()

def create_connection():
    connection = mysql.connector.connect(
        host = '',
        user = '',
        password = '',
        database = ''
    )
    return connection

def create_user(email, password):
    try:
        password = ph.hash(password)
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO BankUser (email, bank_password) VALUES (%s, %s)
"""
        cursor.execute(query, (email, password))
        connection.commit()
        return True
    except Exception as e:
        return False
    finally:
        cursor.close()
        connection.close()

def get_user(email, password):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        SELECT bank_password FROM BankUser WHERE email = %s
"""
        cursor.execute(query, (email, ))
        hashed_password = cursor.fetchone()[0]
        ph.verify(hashed_password, password)
        cursor.close()
        connection.close()
        return email
    except Exception as e:
        return None    

def does_email_exist(email):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        SELECT email FROM BankUser WHERE email = %s
"""
        cursor.execute(query, (email, ))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        return False if user is None else True
    except Exception as e:
        return False 


