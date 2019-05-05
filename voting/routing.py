from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

# TODO: implement pages
@app.route('/')
def landing_page():
    return render_template('landing.html')

@app.route('/election/create', methods=['GET','POST'])
def create_election():
    if request.method == 'GET':
        assert request.method == 'GET'
        return 'election creation page'
        # create_election(request)
        # TODO: implement election creation page
    else:
        pass
        return 'election created'
        # TODO implement election creation in DB

@app.route('/election/<election_id>', methods=['GET'])
def see_election(election_id):
    assert request.method == 'GET'

@app.route('/election/<election_id>/vote', methods=['GET', 'POST'])
def vote(election_id):
    if request.method == 'GET':
        return "CAST VOTE HERE"
        # display voting page
    else:
        assert request.method == 'POST'
        return ""
