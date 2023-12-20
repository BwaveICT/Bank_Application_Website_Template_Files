from app import app
from flask import render_template


@app.route('/deposit')
def deposit():
     return render_template('user/deposit.html')
