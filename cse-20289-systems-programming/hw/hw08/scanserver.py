from flask import Flask, request, send_file, abort
from datetime import datetime
import time
import os
import subprocess

app = Flask(__name__)

@app.route('/scanner', methods=['POST'])
def scanner():
    #get scanning directory arg in post
    toscan = request.args.get('toscan')
    log = request.args.get('log')

    #check for proper args
    if not toscan:
        abort(400, description="Missing toscan argument")

    if not log:
        abort(400, description="Missing log argument")

    if 'file' not in request.files:
        abort(400, description="No file specified in request")

    file = request.files['file']

    if not os.path.exists(toscan):
        abort(404, description="Scanning directory invalid")

    if not os.path.exists(log):
        abort(404, description="Log directory invalid")

    #save file to scanning directory
    file_path = os.path.join(toscan, file.filename)
    file.save(file_path)

    # Get today's date
    current_date = datetime.today().date()

    log_file = f"{current_date}.log"
    log_file_path = os.path.join(log, log_file)

    time.sleep(3) #sleep to give scanner time to put entry in log

    # Check if the log file exists
    if not os.path.exists(log_file_path):
        abort(404, description="No log file exists, make sure scanner is running")

    # Open and read the log file
    with open(log_file_path, 'r') as log_file_content:
        lines = log_file_content.readlines()

    # Look for the last line in the log with the specified file path
    for line in reversed(lines):
        if file.filename in line:
            return line.strip()
    
    abort(404, description="No log entry found, make sure scanner is running")

if __name__ == '__main__':
    app.run(host='student11.cse.nd.edu', port=54004, debug=True)