from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Welcome to My Flask App!</h1>
    <p>Current Time: {datetime.now()}</p>
    <p>Pod ID: {os.environ.get('HOSTNAME', 'localhost')}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
