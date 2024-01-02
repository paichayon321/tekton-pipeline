from flask import Flask, render_template, request
import os
import random
import signal
import sys

if len(sys.argv) != 2:
    print("Usage: python approval.py approvecode ")
    sys.exit(1)

tempcode = sys.argv[1]   

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/approvepage')
def approvepage();
    return render_template('approve.html')

@app.route('/process', methods=['POST'])
def process():
    approval_code = request.form['approval_code']
    action = request.form['action']
    print("TempCode: ", tempcode)    

    # You can add your logic here based on the action (approve or reject)
    if action == 'approve':
        # Perform approval logic
        if approval_code == tempcode:
          result = f'Approval code {approval_code} action approved.'
          os.system('echo approve > result.txt')
          return render_template('result.html', result=result)
        else:
          result = f'Invalid approve code'
    elif action == 'reject':
        # Perform rejection logic

        if approval_code == tempcode:
          result = f'Approval code {approval_code} action rejected.'
          os.system('echo reject > result.txt')
          return render_template('result.html', result=result)
    else:
        result = 'Invalid action.'

    return render_template('index.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    # This function will be called when the "Done" button is clicked
    print("Shutting down the Flask server...")
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

