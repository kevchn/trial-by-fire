from flask import Flask, jsonify, abort, make_response, request
from compute import run_submission

from time import time

app = Flask(__name__)


# JSON Error (not HTML)
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# User Specific Routes
@app.route('/users/<int:user_id>/submissions/<int:problem_id>', methods=['POST'])
def create_submission(user_id: int, problem_id: int):
    '''
    Submit a user's code for their problem and get back the result
    '''
    if not request.json:
        abort(400)
    
    start_time = time()
    submission_result: bool = run_submission(problem_id, request.json['code'])
    end_time = time()

    # get submission runtime (0 if error)
    submission_runtime = round(end_time - start_time, 5)
    submission_runtime = submission_runtime if submission_runtime > 0 else 0

    response = [
        {
            'success': submission_result,
            'runtime': submission_runtime
        }
    ]
    return jsonify({'submission': response}), 201


@app.route('/users/<int:user_id>/solved/', methods=['GET'])
def get_solved(user_id: int):
    '''
    Get solved problems by user
    '''
    if not user_id in range(len(users)):
        abort(404)
    return jsonify({'solved': users[user_id]['solved']})


# Global Routes
@app.route('/problems/<int:problem_id>', methods=['GET'])
def get_problems(problem_id: int):
    '''
    Get global problems and their descriptions
    '''
    if problem_id not in range(len(problems)):
        abort(404)
    return jsonify({'problems': problems[problem_id]})


#TODO: Move to database
problems = [
    {
        'id': 0,
        'title': u'Reverse words in a given string',
        'input': u'The first line contains T denoting the number of testcases. Then follows description of testcases. Each case contains a string containing spaces and characters.',
        'output': u'For each test case, output a single line containing the reversed String.',
        'constraints': [u'1<=T<=20', u'1<=Length of String<=2000'],
        'difficulty': u'Easy',
        'complete': False
    },
    {
        'id': 1,
        'title': u'Next larger element',
        'input': u'The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A[ ].',
        'output': u'For each test case, print in a new line, the next greater element for each array element separated by space in order.',
        'difficulty': u'Medium',
        'complete': False
    }
]

users = [
    {
        'id': 0,
        'name': u'Kevin Chen',
        'solved': [1]
    },
    {
        'id': 1,
        'name': u'Johann Miller',
        'solved': []
    }
]

if __name__ == '__main__':
    app.run(debug=True)