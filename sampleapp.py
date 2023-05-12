from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

#this adds the /domain functionality
#called: Dynamic Routing
# the /name is a "dynamic argument"
@app.route('/<name>')
def print_name(name):
    return 'Welcome , {}'.format(name)


#debug mode
#export FLASK_DEBUG
#if not, add debug=true in the main
if __name__ == '__main__':
    app.run(debug=True)