SITE_TITLE="Web Application"

DB_HOST="localhost"
DB_PORT=3306
DB_NAME="webapp_db"
DB_USER="testuser"
DB_PASSWORD="testpassword"

def DB_CONFIG():
    return {
        "host": DB_HOST,
        "port": DB_PORT,
        "db": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD
    }