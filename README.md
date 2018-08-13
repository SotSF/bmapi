yay it's a bmapi mirror server.

Expects data in json files at these locations:

```
data/art_2016.json
data/art_2017.json
data/art_2018.json
data/camp_2016.json
data/camp_2017.json
data/camp_2018.json
data/event_2016.json
data/event_2017.json
data/event_2018.json
```

Fetching data from the official api:

```
apikey=################################
for type in art camp event; do for year in {2018..2016}; do curl -v -u "${apikey}:" -v "https://api.burningman.org/api/v1/${type}?year=${year}" -o data/${type}_${year}.json; done; done
```

These are from the official burning man api

The root path should have the same behavior as hitting endpoints at the official burning man api v1.

Docs for that are here: https://api.burningman.org/api/docs/v1#

TODO:

* search for each category of data
