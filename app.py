from flask import Flask, send_from_directory, request, jsonify
import os
import subprocess
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///code_files.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CodeFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    filename = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# ✅ Debug Route to Check Favicon
@app.route('/check-favicon')
def check_favicon():
    file_path = os.path.join(app.root_path, 'assets/images/favicon.ico')
    if os.path.exists(file_path):
        return f"Favicon found at {file_path}"
    else:
        return "Favicon NOT found!", 404

# ✅ Fix for Favicon Issue
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'assets/images'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return "Smart Compiler Backend is Running!"

@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.json
    code = data.get("code")
    language = data.get("language")

    file_id = str(uuid.uuid4())[:8]
    extensions = {"python": "py", "cpp": "cpp", "java": "java"}

    if language not in extensions:
        return jsonify({"error": "Unsupported language"}), 400

    filename = f"code_{file_id}.{extensions[language]}"
    filepath = f"/tmp/{filename}"

    with open(filepath, "w") as f:
        f.write(code)

    docker_commands = {
        "python": f"docker run --rm -v /tmp:/tmp python:3.9 python /tmp/{filename}",
        "cpp": f"docker run --rm -v /tmp:/tmp gcc:latest sh -c 'g++ /tmp/{filename} -o /tmp/a.out && /tmp/a.out'",
        "java": f"docker run --rm -v /tmp:/tmp openjdk:11 sh -c 'javac /tmp/{filename} && java -cp /tmp {filename.split('.')[0]}'"
    }

    try:
        result = subprocess.run(
            docker_commands[language], shell=True, capture_output=True, text=True, timeout=5
        )
        output = result.stdout if result.returncode == 0 else result.stderr
    except subprocess.TimeoutExpired:
        output = "Execution timeout!"

    os.remove(filepath)from flask import Flask, send_from_directory, request, jsonify
import os
import subprocess
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///code_files.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CodeFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    filename = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# ✅ Debug Route to Check Favicon Exists
@app.route('/check-favicon')
def check_favicon():
    file_path = os.path.join(app.root_path, 'assets/images/favicon.ico')
    if os.path.exists(file_path):
        return f"Favicon found at {file_path}"
    else:
        return "Favicon NOT found!", 404

# ✅ Fix for Favicon Not Found Issue
@app.route('/favicon.ico')
def favicon():
    return send_from_directory("assets/images", "favicon.ico", mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return "Smart Compiler Backend is Running!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5004)  # ✅ Port 5004

    return jsonify({"output": output})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5004)  # ✅ Set to port 5004
