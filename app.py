import os
import json

from chalice import Chalice

app = Chalice(app_name='mannayo')


filename = os.path.join(
    os.path.dirname(__file__), 'chalicelib', 'voting_result.json')
with open(filename) as f:
    voting_result = json.load(f)

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
        'todo_1': '파일로 저장하기',
        'todo_1_1': 'elasticache 쓰려고 했는데 VPC설정이니 너무 귀찮아서 일단 S3...',
        'todo_2': '필요한 method 정의하기',        
    }
