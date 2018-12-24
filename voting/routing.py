from flask import Flask
from flask import request
app = Flask(__name__)

# TODO: implement pages
@app.route('/')
def landing_page():
    return 'Hello World'

@app.route('/election/create/', methods=['GET','POST'])
def create_election():
    if request:method == 'POST':
        assert request.method == 'POST'
        # create_election(request)
        # TODO: implement election creation
    else:
        pass
        # return election_creation_page()
        # TODO: implement election page

@app.route('/vote/<election_id>/', methods=['GET', 'POST'])
def vote(election_id):
    if request.method == 'POST':
        assert request.method == 'POST'
        # TODO: implement cast_vote
        # return cast_vote(election_id, request)
    else:
        assert request.method == 'GET'
        # TODO: implement ballot screen
