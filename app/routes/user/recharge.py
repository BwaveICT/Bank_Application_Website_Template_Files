from app import app
from flask import render_template



@app.route('/recharge')
def recharge():
     return render_template('user/recharge.html')