from app import app
from flask import render_template

@app.route('/exchange_rate')
def exchange_rate():
     return render_template('user/soon.html')