import json
import time

import spotipy
import spotipy.util as util
from google.cloud import bigquery
from google.cloud.exceptions import NotFound

scope = 'user-read-recently-played'
# 3 hours
time_delay = 7200.0


class BQWriter:

    table_schema = (
        bigquery.SchemaField('Name', 'STRING'),
        bigquery.SchemaField('Duration', 'INTEGER'),
        bigquery.SchemaField('IsExplicit', 'BOOLEAN'),
        bigquery.SchemaField('Id', 'STRING'),
        bigquery.SchemaField('Uri', 'STRING'),
        bigquery.SchemaField('Artists', 'STRING'),
        bigquery.SchemaField('MainArtistName', 'STRING'),
        bigquery.SchemaField('MainArtistId', 'STRING'),
        bigquery.SchemaField('Album', 'STRING'),
        bigquery.SchemaField('AlbumId', 'STRING'),
        bigquery.SchemaField('PlayedAt', 'STRING'),
    )

    def __init__(self, project, dataset_name, table_name,
                 spotify_username) -> None:
        self.project = project
        self.dataset_name = dataset_name
        self.table_name = table_name
        self.table_id = '{}.{}.{}'.format(self.project, self.dataset_name,
                                          self.table_name)
        self.spotify_username = spotify_username
        self.client = bigquery.Client(self.project)

        try:
            self.client.get_dataset(self.dataset_name)
        except NotFound:
            print("Dataset {} is not found. Creating it.".format(
                self.dataset_name))
            dataset = bigquery.Dataset(self.dataset_name)
            dataset.location = "US"
            self.client.create_dataset(dataset)

        try:
            self.client.get_table(self.table_id)
        except NotFound:
            print("Table {} is not found. Creating one".format(table_name))
            table = bigquery.Table(self.table_id, schema=self.table_schema)
            self.client.create_table(table)
            # It takes some time after creating the table
            # before you can use it:
            # https://github.com/googleapis/google-cloud-go/issues/975
            time.sleep(30)

    def get_latest_played_songs(self) -> None:
        start_time = time.time()
        # keep track of the last time an API called was performed.
        # Initialize it with current time
        last_insert_time = int(round(time.time() * 1000))
        errors = None

        while True:
            token = util.prompt_for_user_token(self.spotify_username, scope)
            sp = spotipy.Spotify(auth=token)
            rows = []
            print('Executing at {}'.format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
            songs = sp.current_user_recently_played(after=1659219047000)
            for song in songs['items']:
                rows.append(
                    (song['track']['name'], song['track']['duration_ms'],
                     song['track']['explicit'],
                     song['track']['id'], song['track']['uri'],
                     json.dumps(song['track']['artists']),
                     song['track']['artists'][0]['name'],
                     song['track']['artists'][0]['id'],
                     song['track']['album']['name'],
                     song['track']['album']['uri'], song['played_at']))

            print('results for last_insert_time {} are {}'.format(
                last_insert_time, len(rows)))
            if len(rows) > 0:
                errors = self.client.insert_rows(self.table_id, rows,
                                                 self.table_schema)

            if not errors:
                print('{} records inserted'.format(len(rows)))
                last_insert_time = int(round(time.time() * 1000))
            else:
                print(errors)
            # code will be executed every time_delay seconds
            time.sleep(time_delay - ((time.time() - start_time) % time_delay))
