import os
from flask import Flask, request, jsonify
import shutil
import subprocess
import tempfile

# Initialize Flask app
app = Flask(__name__)

# Define directory locations (these could be set via environment variables or configuration)
WATCH_DIR = "scandata/toscan"
APPROVED_DIR = "scandata/approved"
QUARANTINE_DIR = "scandata/quarantined"
MALICIOUS_URLS_CSV = "badsites/badsite-100.csv"
LOG_DIR = "scandata/log"

# Create necessary directories if they don't exist
os.makedirs(WATCH_DIR, exist_ok=True)
os.makedirs(APPROVED_DIR, exist_ok=True)
os.makedirs(QUARANTINE_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Function to handle file extraction
def extract_archive(archive, destination):
    try:
        if archive.endswith(('.tar.gz', '.tar')):
            subprocess.run(['tar', '-xf', archive, '-C', destination], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif archive.endswith('.zip'):
            subprocess.run(['unzip', archive, '-d', destination], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            raise ValueError("Unsupported archive format")
    except Exception as e:
        return False, str(e)
    return True, None

# Function to check for malicious URLs (similar to `check_malicious_urls` in scanner.sh)
def check_malicious_urls(file_path):
    with open(MALICIOUS_URLS_CSV, 'r') as url_file:
        malicious_urls = url_file.read().splitlines()
        for url in malicious_urls:
            with open(file_path, 'r') as f:
                if url in f.read():
                    return True, url
    return False, None

# Function to check for sensitive content (similar to `check_sensitive_content` in scanner.sh)
def check_sensitive_content(file_path):
    with open("sensitive_keywords.txt", 'r') as f:
        sensitive_keywords = f.read().splitlines()
        for keyword in sensitive_keywords:
            with open(file_path, 'r') as file:
                if keyword.lower() in file.read().lower():
                    return True, keyword
    return False, None

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file to the 'toscan' directory
    filepath = os.path.join(WATCH_DIR, file.filename)
    file.save(filepath)

    # Temporary directory for extraction
    temp_dir = tempfile.mkdtemp()

    # Extract the archive
    success, error = extract_archive(filepath, temp_dir)
    if not success:
        # If extraction fails, quarantine the file
        reason_file = os.path.join(QUARANTINE_DIR, f"{file.filename}.reason")
        with open(reason_file, 'w') as reason:
            reason.write(f"{file.filename}\nCANNOTEXTRACT\n{error}")
        return jsonify({"status": "quarantined", "reason": "CANNOTEXTRACT", "error": error}), 400

    # Scan the extracted files for malicious URLs or sensitive content
    for root, dirs, files in os.walk(temp_dir):
        for extracted_file in files:
            file_path = os.path.join(root, extracted_file)

            # Check for malicious URLs
            is_malicious, malicious_url = check_malicious_urls(file_path)
            if is_malicious:
                reason_file = os.path.join(QUARANTINE_DIR, f"{file.filename}.reason")
                with open(reason_file, 'w') as reason:
                    reason.write(f"{extracted_file}\nMALICIOUSURL\n{malicious_url}")
                shutil.move(filepath, QUARANTINE_DIR)
                return jsonify({"status": "quarantined", "reason": "MALICIOUSURL", "url": malicious_url}), 400

            # Check for sensitive content
            is_sensitive, sensitive_content = check_sensitive_content(file_path)
            if is_sensitive:
                reason_file = os.path.join(QUARANTINE_DIR, f"{file.filename}.reason")
                with open(reason_file, 'w') as reason:
                    reason.write(f"{extracted_file}\nSENSITIVE\n{Sensitive_content}")
                shutil.move(filepath, QUARANTINE_DIR)
                return jsonify({"status": "quarantined", "reason": "SENSITIVE", "sensitive_content": sensitive_content}), 400

    # If all checks pass, move the file to the approved directory
    shutil.move(filepath, APPROVED_DIR)

    return jsonify({"status": "approved", "message": f"{file.filename} is approved."}), 200

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
