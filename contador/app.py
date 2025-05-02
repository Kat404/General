from flask import Flask, jsonify, request

app = Flask(__name__)

# Contador global
contador = 0

@app.route('/contador', methods=['GET'])
def get_contador():
    return jsonify({'contador': contador})

@app.route('/contador/incrementar', methods=['POST'])
def incrementar():
    global contador
    contador += 1
    return jsonify({'contador': contador})

@app.route('/contador/decrementar', methods=['POST'])
def decrementar():
    global contador
    contador -= 1
    return jsonify({'contador': contador})

if __name__ == '__main__':
    app.run(debug=True)
