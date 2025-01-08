from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'mysql_db',
    'user': 'root',
    'password': 'password',
    'database': 'flask_db'
}

# Route to fetch data from database
@app.route('/')
def index():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
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
