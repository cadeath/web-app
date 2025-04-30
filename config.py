import mysql.connector

SITE_TITLE="Web Application"

DB_HOST="192.168.1.66"
DB_PORT=3306
DB_NAME="webapp_db"
DB_USER="testuser"
DB_PASSWORD="testpassword"

def db_connection():
    cnx = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    return cnx