'''
Main file to run the server
'''

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from analysis import Analysis
from API_requests import Requests

# initialize Flask
app = Flask(__name__)
CORS(app)


@app.route('/api/get_available_leagues', methods=['GET'])
def get_available_leagues():
    '''
    Get all available leagues.
    '''
    available_leagues = Requests.get_available_leagues()

    return make_response(jsonify(available_leagues), 200)


@app.route('/api/get_teams_by_league_id', methods=['POST'])
def get_teams_by_league_id():
    '''
    Get all teams in league by its id.
    '''
    request_data = request.json

    league_id = request_data['league_id']
    teams = Requests.get_teams_by_league_id(league_id)

    return make_response(jsonify(teams), 200)


if __name__ == '__main__':
    app.run(debug=True)
