from flask import Flask, request, abort
import json

app = Flask(__name__)

class Year(object):
    def __init__(self, year: int):
        self.art = Year.parse_file('data/art_{year}.json'.format(year=year))
        self.camp = Year.parse_file('data/camp_{year}.json'.format(year=year))
        self.event = Year.parse_file('data/event_{year}.json'.format(year=year))

    @staticmethod
    def parse_file(fpath: str):
        with open(fpath, 'r') as f:
            raw = json.load(f)
        return { d['uid']: d for d in raw }

years = {
    '2016': Year(2016),
    '2017': Year(2017),
    '2018': Year(2018),
}

def index(endpoint):
    year = request.args['year']
    data = years[year]
    return json.dumps(list(getattr(data, endpoint).values()))

@app.route('/art')
def art_index():
    return index('art')

@app.route('/camp')
def camp_index():
    return index('camp')

@app.route('/event')
def event_index():
    return index('event')

def show(endpoint, uuid):
    for year in years.values():
        if uuid in getattr(year, endpoint):
            return json.dumps(getattr(year, endpoint)[uuid])
    return abort(404)

@app.route('/art/<uuid>')
def art_show(uuid):
    return show('art', uuid)

@app.route('/camp/<uuid>')
def camp_show(uuid):
    return show('camp', uuid)

@app.route('/event/<uuid>')
def event_show(uuid):
    return show('event', uuid)

app.run(port=5000, debug=True)
