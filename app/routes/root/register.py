from app import app
from flask import render_template


@app.route('/register')
def register_page():
    return render_template('root/register.html')
