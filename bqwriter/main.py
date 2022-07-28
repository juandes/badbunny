from bqwriter import BQWriter
import argparse

if __name__ == '__main__':
    print("Starting data collector...")
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('--project', help='GCP project name')
    parser.add_argument('--dataset', help='BigQuery dataset name')
    parser.add_argument('--table', help='BigQuery table name')
    parser.add_argument('--username', help='Spotify Username')
    args = parser.parse_args()
    bqWriter = BQWriter(args.project, args.dataset, args.table, args.username)
    bqWriter.get_latest_played_songs()