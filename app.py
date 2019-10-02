from dataclasses import asdict, dataclass, field
from dateutil.parser import parse
from typing import List
import json
import os
import uuid

import boto3

from chalice import Chalice

app = Chalice(app_name='mannayo')
_DB = None


@dataclass
class Meeting:
    title: str  # unique key
    when: str
    why: str = ''
    who: List[str] = field(default_factory=list)
    where: str = ''


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

    when = parse(json['when']).strftime('%Y-%m-%d')
    title = uuid.uuid4().hex[:8]  # Create meeting_id
    meeting = Meeting(
        title=title,
        when=when,
        why=json.get('why'),
        who=json.get('who'),
        where=json.get('where'),
    )

    db = get_db()
    response = db.put_item(
        Item=asdict(meeting)
    )
    return title


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
