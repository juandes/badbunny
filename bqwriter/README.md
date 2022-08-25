# BQWriter

This directory contains the script that reads from Spotify and writes to BigQuery. To use it, you need to export the environment variables `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URL` and set their values with your Spotify client ID, client secret, and redirect URL. Also, you execute the script using the following arguments:

- `project`: the Google Cloud Platform project with the BigQuery where you will write the Spotify data.
- `dataset`: the BigQuery dataset where you will write the Spotify data.
- `table`: the table within the dataset where you will write the Spotify data.
- `username`: your Spotify username.


For example:

```
SPOTIPY_CLIENT_ID=XXXXX SPOTIPY_CLIENT_SECRET=XXXXX SPOTIPY_REDIRECT_URI=http://localhost/ \ python3 main.py --project=your-gcp-project --dataset=your_table_dataset --table=your_table --username=your_spotify_username
```

For more information about the authorization code flow, see: https://spotipy.readthedocs.io/en/master/#authorization-code-flow