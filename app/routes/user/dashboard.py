from app import app
from flask import render_template

@app.route('/dashboard')
def dashboard():
     return render_template('user/index.html')






