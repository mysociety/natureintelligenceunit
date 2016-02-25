#!/usr/bin/env python
import psycopg2
import psycopg2.extras
import json
import requests

DBNAME = "niu"
TABLES = ('landuse', 'natural')
FEATURE_TYPES = str((
    'grass', 'allotments', 'park', 'flower_bed', 'flowerbed',
    'garden', 'gardern', 'grass', 'green', 'greenfield', 'greenspace',
    'meadow', 'natural', 'natural_reserve', 'orchard', 'paddock',
    'pasture', 'plants', 'playing_fields', 'pond', 'recreational',
    'reservoir', 'village_green', 'woodland'
))
QUERY = """SELECT
n.name, n.type, ST_AsGeoJSON(n.wkb_geometry) geom, n.osm_id
FROM "{{table}}" n, wards w
WHERE w.UNIT_ID = %s
AND n.type IN {types}
AND ST_Intersects(n.wkb_geometry, w.wkb_geometry)
""".format(types=FEATURE_TYPES)

cursor = None

def db_connect():
    global cursor
    connection = psycopg2.connect(dbname=DBNAME)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

def get_features_for_unit_id(uid):
    cursor or db_connect()
    features = []
    for table in TABLES:
        cursor.execute(QUERY.format(table=table), (uid, ))
        for row in cursor:
            geometry = json.loads(row['geom'])
            features.append({
                'type': 'Feature',
                'geometry': geometry,
                'properties': {k: v for k, v in row.items() if k != 'geom'},
                'id': row['osm_id'],
            })
    return features

def write_geojson(mid, uid):
    output = {
        "type": "FeatureCollection",
        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
        "features": get_features_for_unit_id(uid)
    }
    with open("fixmystreet/web/greenspaces/{}.geojson".format(mid), "w") as f:
        json.dump(output, f)


def get_id_mapping():
    lbw = requests.get("http://mapit.mysociety.org/areas/LBW.json").json()
    yield from ((k, v['codes']['unit_id']) for k, v in lbw.items())

def main():
    for mapit_id, unit_id in get_id_mapping():
        write_geojson(mapit_id, unit_id)

if __name__ == '__main__':
    main()