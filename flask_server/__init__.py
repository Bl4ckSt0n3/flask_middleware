from flask import Flask, request
from middleware import Middleware

# create app from Flask
app = Flask(__name__)

# call middleware
app.wsgi_app = Middleware(app.wsgi_app)

# code api
@app.route('/', methods=['GET', 'POST'])
def hello():
    # define environ['user']
    user = request.environ['user']
    return f"Hi {user['name']}"
