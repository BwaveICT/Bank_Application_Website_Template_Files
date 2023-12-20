from app import app
from flask import render_template


@app.route('/transaction_history')
def transaction_history():
    return render_template('user/transaction_history.html')
