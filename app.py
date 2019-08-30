import json
import os

import boto3

from chalice import Chalice

app = Chalice(app_name='mannayo')
_DB = None


@app.route('/vote/{meeting_id}', methods=['PATCH'])
def vote(meeting_id):
    try:
        voting_data = voting_result[meeting_id]
    except KeyError:
        return {'message': 'id는 어디'}
    print(f'test: {voting_data}')

    json = app.current_request.json_body
    username = json['username']
    attend = '참석' if json['attend'] else '못감'
    return {'message': f'{username}: {attend}'}


@app.route('/meeting', methods=['POST'])
def meeting():
    json = app.current_request.json_body
    candidate_dates = json['candidate_dates']
    # TODO: Create meeting on cadate_dates
    print(candidate_dates)
    return {'message': 'Meeting(id: {}) 이 생성되었습니다'.format(1)}


@app.route('/')
def todo():
    return {
        'todo_1': '필요한 method 정의하기',
        'todo_2': 'Test가능하도록 하고 Test 추가',
    }


def get_db():
    global _DB
    if _DB is None:
        _DB = boto3.resource('dynamodb').Table(os.environ['MANNAYO_TABLE_NAME'])
    return _DB


@app.route('/user', methods=['POST'])
def add_user():
    json = app.current_request.json_body
    username = json['name']
    db = get_db()
    response = db.put_item(
        Item={
            'user': username,
        }
    )
    return response

@app.route('/user', methods=['GET'])
def user():
    json = app.current_request.json_body
    username = json['name']
    db = get_db()
    response = db.get_item(
        Key={
            'user': username,
        }
    )
    item = response.get('Item')
    if item:
        return item
    return 'No item'


@app.route('/test-ddb')
def test_ddb():
    resource = boto3.resource('dynamodb')
    table = resource.Table(os.environ['MANNAYO_TABLE_NAME'])
    return table.name
