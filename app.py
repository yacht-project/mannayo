from dataclasses import asdict, dataclass, field
from dateutil.parser import parse
from typing import Dict, List
import json
import os
import uuid

import boto3

from chalice import Chalice, CORSConfig


app = Chalice(app_name='mannayo')
_DB = None

cors_config = CORSConfig(
    allow_origin='*',
)


@dataclass
class Meeting:
    title: str  # unique key
    when: Dict[str, Dict[str, str]]  # {'from': '', 'to': ''}
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


@app.route('/meeting', methods=['POST'], cors=cors_config)
def create_meeting():
    json = app.current_request.json_body

    try:
        from_ = parse(json['when']['from']).strftime('%Y-%m-%d')
        to_ = parse(json['when']['to']).strftime('%Y-%m-%d')
    except ValueError:
        return ''

    title = uuid.uuid4().hex[:8]  # Create meeting_id
    meeting = Meeting(
        title=title,
        when={'from': from_, 'to': to_},
        why=json.get('why'),
        who=json.get('who'),
        where=json.get('where'),
    )

    db = get_db()
    response = db.put_item(
        Item=asdict(meeting)
    )
    return title


@app.route('/meeting/{meeting_id}', methods=['PATCH'], cors=cors_config)
def change_users(meeting_id):
    json = app.current_request.json_body
    users = json['who']

    db = get_db()
    try:
        response = db.get_item(
            Key={
                'title': meeting_id,
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])

    try:
        item = response['Item']
    except KeyError:
        return ''

    item['who'] = users
    db.put_item(
        Item=item
    )
    return item


@app.route('/meeting/{meeting_id}', methods=['GET'], cors=cors_config)
def list_meeting(meeting_id):
    db = get_db()
    response = db.get_item(
        Key={
            'title': meeting_id,
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
