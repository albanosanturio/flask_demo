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


@app.route('/landing', methods = ['GET','POST'])

def landing():
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
        return 'Not developed yet', 201





@app.route('/books', methods= ['GET','POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
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
    


if __name__ == '__main__':
    app.run(debug=True)