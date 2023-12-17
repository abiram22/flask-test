from flask import Flask, render_template
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


password = os.environ.get('db_password')

# Use the password in your code
# ...

application = Flask(__name__)

# Configure MySQL
db = mysql.connector.connect(
    host="database-1.cqrkaem5rqpp.eu-north-1.rds.amazonaws.com",
    user="admin",
    password=password,
    database="ipl"
)

@application.route('/')
def index():
    # Use the connection to execute a query
    cursor = db.cursor()
    print('ll')
    cursor.execute("SELECT * FROM player_info where player_name like 'v%'")
    data = cursor.fetchall()

    # Pass the data to your template
    return render_template('index.html', data=data)

if __name__ == '__main__':
    application.run()
