from flask import Flask, render_template, request, redirect, url_for
from database.db_connector import get_db
import os
app = Flask(__name__, template_folder='web/templates')

app.config['MONGO_URI'] = os.getenv("MONGO_URI", "mongodb://localhost:27017/decepticoders")

# Mongo connection
db = get_db(app.config['MONGO_URI'])

@app.route('/')
def dashboard():
    alerts = db['alerts'].find().sort("timestamp", -1)
    return render_template('dashboard.html', alerts=alerts)

@app.route('/create-test-alert')
def create_test_alert():
    test_alert = {
        "message": "🔥 Intrusion Detected: Port Scan from 192.168.1.100",
        "timestamp": "2025-07-04 12:00:00"
    }
    db['alerts'].insert_one(test_alert)
    return "Test alert inserted!"

@app.route('/alerts')
def alert_view():
    alerts = db['alerts'].find().sort("timestamp", -1)
    return render_template('alerts.html', alerts=alerts)

@app.route('/log', methods=['POST'])
def log_decoy():
    data = request.json
    db['decoy_logs'].insert_one(data)
    return {'status': 'logged'}, 201

if __name__ == '__main__':
    app.run(debug=True)
