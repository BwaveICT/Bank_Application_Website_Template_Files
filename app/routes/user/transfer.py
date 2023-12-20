from app import app
from flask import render_template


@app.route('/transfer')
def transfer():
     return render_template('user/transfer.html')


