from flask import Flask, request, jsonify

app = Flask(__name__)

#@app.route('/')
#def index():
#    return 'Hello World'

#this adds the /domain functionality
#called: Dynamic Routing
# the /name is a "dynamic argument"

#@app.route('/<name>')
#def print_name(name):
#    return 'Welcome , {}'.format(name)

books_list = [
  {
    "id": 0,
    "author": "Chinua Achebe",
    "language": "English",
    "title": "Things Fall Apart",
  },
  {
    "id": 1,  
    "author": "Hans Christian Andersen",
    "language": "Danish",
    "title": "Fairy tales",
  },
  {
    "id": 2,  
    "author": "Dante Alighieri",
    "language": "Italian",
    "title": "The Divine Comedy",
  },
  {
    "id": 3,  
    "author": "Unknown",
    "language": "Akkadian",
    "title": "The Epic Of Gilgamesh",
  },
  {
    "id": 4,        
    "author": "Unknown",
    "language": "Hebrew",
    "title": "The Book Of Job",
  },
]


@app.route('/books', methods = ['GET','POST'])

def books():
    if request.method == 'GET':
        if len(books_list) > 1:
            return jsonify(books_list)
        else:
            return 'Nothing found', 404
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        iD = books_list[-1]['id']+1
        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_lang,
            'title': new_title
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201


@app.route('/book/<int:id>', methods =['GET','PUT','DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book["id"] == id:
                return jsonify(book)
            pass
    if request.method == 'PUT':
        for book in books_list:
            if book["id"] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_book = {
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title']
                }
                return jsonify(updated_book)
    
    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)


if __name__ == '__main__':
    app.run(debug=True)