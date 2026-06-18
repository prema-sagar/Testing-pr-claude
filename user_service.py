# ================================================================
# FILE: sample-app/user_service.py
#
# This file has INTENTIONAL bugs for the POC demo.
# Claude will detect both as CRITICAL and block the merge.
#
# Bug 1 — SQL Injection (line 18): user input directly in query
# Bug 2 — Hardcoded Secret (line 26): production API key in code
# ================================================================

import sqlite3


def get_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # SQL injection vulnerability — user input directly in query string
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()


def authenticate(user, password):
    # Hardcoded production API key — critical security issue
    api_key = "sk-prod-abc123xyz789secret"
    stored_password = "admin123"
    return password == stored_password


def get_all_users():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
