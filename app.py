from flask import Flask, request, send_file, jsonify
from aes_crypto import encrypt_file, decrypt_file, get_key
from werkzeug.utils import secure_filename
import os
import io

app = Flask(__name__)

@app.route("/encrypt", methods=["POST"])
def encrypt():
    uploaded_file = request.files["file"]
    user_key = request.form["key"]
    key = get_key(user_key)
    data = uploaded_file.read()
    encrypted_data = encrypt_file(data, key)
    return send_file(io.BytesIO(encrypted_data), as_attachment=True, download_name="encrypted.aes")

@app.route("/decrypt", methods=["POST"])
def decrypt():
    uploaded_file = request.files["file"]
    user_key = request.form["key"]
    key = get_key(user_key)
    data = uploaded_file.read()
    try:
        decrypted_data = decrypt_file(data, key)
    except ValueError:
        return jsonify({"error": "Sai khóa hoặc file bị lỗi!"}), 400
    return send_file(io.BytesIO(decrypted_data), as_attachment=True, download_name="decrypted.txt")

if __name__ == "__main__":
    app.run(debug=True)
