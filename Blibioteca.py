from flask import Flask, jsonify, request

books = {
    'numero' : ['0'],
    'titulo' : ['O escaravelho do diabo'],
    'autor' : ['Autor 1'],
    'edicao' : ['3 edicao'],
    'controle' : ['Emprestado']
    }

def showBooks() :
    return True

def createBook(titulo, autor, edicao, controle) :
    return True

def updateBook(numero) :
    return True

def deleteBook(numero) :
    return True

def bookStatus(numero) :
    return True


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def booksFunction() :
    if request.method == 'GET' :
        result = showBooks()
        if result :
            return jsonify(message="Livros que estao no sistema"), 201
        else :
            return jsonify(message='Comando não executado'), 401

    elif request.method == 'POST' :
        titulo = request.args.get('titulo', '')
        autor = request.args.get('autor', '')
        edicao = request.args.get('edicao', '')
        controle = request.args.get('controle', '')
        result = createBook(titulo, autor, edicao, controle)
        if result :
            return jsonify(message="Livro criado" ), 201
        else :
            return jsonify(message='Comando não executado'), 401


@app.route('/biblioteca', methods=['GET', 'PUT', 'DELETE'])
def bookFunctionId() :
    if request.method == 'GET' :
        numero = request.args.get('numero', '')
        result = bookStatus(numero)
        if result :
            return jsonify(message="Status do livro" ), 200
        else :
            return jsonify(message='Comando não executado'), 401

    elif request.method == 'PUT' :
        numero = request.args.get('numero', '')
        titulo = request.args.get('titulo', '')
        autor = request.args.get('autor', '')
        edicao = request.args.get('edicao', '')
        result = updateBook(numero, titulo, autor, edicao)
        if result :
            return jsonify(message="Livro atualizado" ), 200
        else :
            return jsonify(message='Comando não executado'), 401

    elif request.method == 'DELETE' :
        numero = request.args.get('numero', '')
        deleteBook(numero)
        result = showBooks()
        if result :
            return jsonify(message="Livro deletado" ), 200
        else :
            return jsonify(message='Comando não executado'), 401


if __name__ == '__main__' :
    app.run()
