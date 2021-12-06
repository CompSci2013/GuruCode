import boto3
import subprocess

def lambda(s,d,c):

    session = boto3.Session()


def sync_ddb_table(source_ddb, destination_ddb):
    response = source_ddb.scan(
            TableName="table1"
            )
