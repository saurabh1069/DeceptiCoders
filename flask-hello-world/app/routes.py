from flask import render_template, request, redirect, url_for, flash, session

import logging

def add_log(message):
    logging.info(message)

def setup_routes(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            if username == 'admin' and password == 'password':
                session['user'] = username
                add_log(f"User '{username}' logged in successfully.")
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password', 'danger')
                add_log(f"Failed login attempt for username '{username}'.")
        return render_template('login.html')

    @app.route('/dashboard')
    def dashboard():
            if 'user' in session:
                with open('logs/app.log', 'r') as f:
                    log_lines = f.readlines()
                return render_template('dashboard.html', user=session['user'], logs=log_lines)
            return redirect(url_for('login'))

    @app.route('/show_logs')
    def show_logs():
        with open('logs/app.log', 'r') as f:
            log_lines = f.readlines()
        # Only include WARNING and ERROR logs
        filtered_logs = [line for line in log_lines if 'WARNING' in line or 'ERROR' in line or 'INFO' in line]
        return render_template('logs.html', logs=filtered_logs)

    @app.route('/AI_Assistant', methods=['GET'])
    def AI_Assistant():
        return render_template('AI_Assistant.html')

    @app.route('/logout', methods=['POST'])
    def logout():
        user = session.pop('user', None)
        if user:
            add_log(f"User '{user}' logged out.")
        return redirect(url_for('login'))
    
