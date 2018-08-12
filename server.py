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

@app.route('/art')
def art_index():
    year = years[request.args['year']]
    return json.dumps(list(year.art.values()))

@app.route('/camp')
def camp_index():
    year = years[request.args['year']]
    return json.dumps(list(year.camp.values()))

@app.route('/event')
def event_index():
    year = years[request.args['year']]
    return json.dumps(list(year.event.values()))

@app.route('/art/<uuid>')
def art_show(uuid):
    for year in years.values():
        if uuid in year.art:
            return json.dumps(year.art[uuid])
    return abort(404)

app.run(port=5000, debug=True)
