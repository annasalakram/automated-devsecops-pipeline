import os
import sqlite3

# 🚨 SECURITY VULNERABILITY 1: Hardcoded Secrets (Credential Leakage)
# CWE-798: Use of Hard-coded Credentials
# This mimics a critical risk where developers mistakenly expose infrastructure keys.
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE" 

def get_user_data():
    """
    Simulates a user data retrieval function that contains severe security flaws.
    This function is designed to be caught by Static Application Security Testing (SAST) tools.
    """
    # Setting up an in-memory database for simulation purposes
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Prompting user input via terminal/console
    user_input = input("Enter username to search: ")
    
    # 🚨 SECURITY VULNERABILITY 2: SQL Injection (SQLi)
    # CWE-89: Improper Neutralization of Special Elements used in an SQL Command
    # Direct string formatting allows an attacker to manipulate the SQL statement structure.
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    
    print(f"[DEBUG] Executing Query: {query}")
    
    try:
        # Running the raw, unvalidated query string against the database
        cursor.execute(query)
    except Exception as e:
        print(f"Execution Error: {e}")

if __name__ == "__main__":
    print("--- DevSecOps Pipeline Test Environment ---")
    get_user_data()
