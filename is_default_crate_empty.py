""" Check if Default Crate is empty on DynamoDB. """

import os

import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key

DEFAULT_DUMMY_USER = 'marq_clickops'


def default_crate_is_empty(table) -> str:
    """ Returns True if default crate is empty in DDB. """
    filtering_exp = Key('UserName').eq(DEFAULT_DUMMY_USER)
    response = table.query(KeyConditionExpression=filtering_exp)
    crate = response['Items'][0]
    video_list = crate['VideoList']
    if len(video_list) == 0:
        return True
    return False
#


def main():
    os.environ['AWS_PROFILE'] = "default"
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
    ddb = resource('dynamodb')
    table = ddb.Table('Crates')
    if default_crate_is_empty(table):
        print('EMPTY')
    else:
        print('FULL')
#

if __name__ == '__main__':
    main()

