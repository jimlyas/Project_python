import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class FireDataExample:
    # noinspection PyUnresolvedReferences
    def __init__(self):
        cred = credentials.Certificate('./services.json')
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://delia-weather.firebaseio.com'})
        ref = db.reference('/mountain')

        snap = ref.get()

        for key, val in snap.items():
            print("index : {0}".format(key))
            print("nama : {0}".format(val['name']))

            print("latitude,longitude : {0},{1}".format(val['latitude'], val['longitude']))
            print('')


if __name__ == '__main__':
    a = FireDataExample()