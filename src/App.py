from flask import Flask, make_response, jsonify, request, config
from db import Produtos

app = Flask(__name__)

@app.route('/Produtos', methods=['GET'])
def getProduct():
    return make_response(
        jsonify(Produtos)
    )

@app.route('/Produtos', methods=['POST'])
def postProduct():
    produtos = request.json
    Produtos.append(produtos)
    return jsonify(produtos)    


if __name__=='__main__':
    app.run()