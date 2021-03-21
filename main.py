import json
from bottle import route, run, template

@route('/', metods='GET')
def home():
    find = open('JSON/data.json')
    data = json.load(find)
    # json.dumps(find)
    for i in data:
        print(i)
        # return f'test response \n {data}'
        return template('views/index.html', rows=data["students"])
    find.close()

run(host='localhost', port=8080, debug=True)