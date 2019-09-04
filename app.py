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


@app.route('/meeting', methods=['POST'])
def create_meeting():
    json = app.current_request.json_body
    title = json['title']
    db = get_db()
    response = db.put_item(
        Item={
            'title': title,
        }
    )
    return response


@app.route('/meeting/{title}', methods=['GET'])
def list_meeting(title):
    db = get_db()
    response = db.get_item(
        Key={
            'title': title,
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
