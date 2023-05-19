# pip overview
Lets list some useful commands to have at hand


pip list

```
Package            Version
------------------ -------
blinker            1.6.2
click              8.1.3
Flask              2.3.2
importlib-metadata 6.6.0
itsdangerous       2.1.2
Jinja2             3.1.2
MarkupSafe         2.1.2
pip                20.0.2
pkg-resources      0.0.0
setuptools         44.0.0
Werkzeug           2.3.4
wheel              0.34.2
zipp               3.15.0
```

pip freeze

```
blinker==1.6.2
click==8.1.3
Flask==2.3.2
importlib-metadata==6.6.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
Werkzeug==2.3.4
zipp==3.15.0
```

# virtualenv overview

In case not installed


```
pip install virtualenv
```

Now create a new env called "myEnv" with python3 version
The source command is used to execute the "activate" script for the new env

```
virtualenv myEnv -p python3
source myEnv/bin/activate
```

1st way for running app (env variable):
```
LINUX:   export FLASK_APP=sampleapp.py
WINDOWS: set FLASK_APP=sampleapp.py
flask run

go to localhost:5000
```


2nd way for running app (app.run):
```
LINUX:   export FLASK_APP=sampleapp.py
WINDOWS: set FLASK_APP=sampleapp.py
flask run

go to localhost:5000
```



# flask init

install the library
```
pip install flask
```

open the python interpreter
and check if it can import flask
```
python
import flask
```
If thats ok we are good to go


# flask commands

try flask --help
```
Commands:
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.
```

try for further help:

```
flask run --help
flask shell --help
flask routes --help
```


#debug mode
#export FLASK_DEBUG
#if not, add debug=true in the main




### context and global variables
Context, makes variables globally accessable

#### application context
current_app
g

app_context.push()

#### request context
request
session

request_context.push()

>>> from sampleapp import app
>>> from flask import current_app
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name

 

>>> app.url_map: lists al routes
Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/' (HEAD, OPTIONS, GET) -> index>,
 <Rule '/<name>' (HEAD, OPTIONS, GET) -> print_name>])

>>> from flask import request
>>> req_ctx=app.request_context()
>>> req_ctx.push()
>>> request.url

Response object methods
.set_cookie()
.delete_cookie()
.set_data()
.get_data()

