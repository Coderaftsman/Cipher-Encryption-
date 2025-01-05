from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Caesar Cipher Logic
def caesar_cipher(text, shift, encrypt=True):
    if not encrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML file

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get('text', '')
    shift = int(data.get('shift', 0))
    encrypted_text = caesar_cipher(text, shift, encrypt=True)
    return jsonify({'result': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    text = data.get('text', '')
    shift = int(data.get('shift', 0))
    decrypted_text = caesar_cipher(text, shift, encrypt=False)
    return jsonify({'result': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
