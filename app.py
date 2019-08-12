from chalice import Chalice

app = Chalice(app_name='mannayo')


@app.route('/vote/{meeting_id}', methods=['PATCH'])
def vote(meeting_id):
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
        'todo_2': '필요한 method 정의하기',        
    }
