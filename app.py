from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'mysql_db',
    'user': 'root',
    'password': 'password',
    'database': 'flask_db'
}

# Function to connect to the database with retries
def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            # Try to connect to MySQL database
            conn = mysql.connector.connect(**db_config)
            return conn
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            retries -= 1
            time.sleep(5)  # Wait for 5 seconds before retrying
    raise Exception("Could not connect to MySQL after several attempts")

# Route to fetch data from database
@app.route('/')
def index():
    try:
        conn = get_db_connection()  # Get the DB connection
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM greetings LIMIT 1;")
        message = cursor.fetchone()[0]
        cursor.close()
        conn.close()
    except Exception as e:
        message = f"Error: {e}"

    return f"<h1>{message}</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

