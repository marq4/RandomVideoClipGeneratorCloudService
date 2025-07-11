""" For now just get the Default Crate for Default User from DDB. """

import os
import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key

DEFAULT_DUMMY_USER = 'marq_clickops'
DEFAULT_CRATE_NAME = 'Default_clickops'


def display_default_crate(table) -> None:
    """ Prints HTML of the Default crate & default dummy 'user' from DDB. """
    filtering_exp = Key('UserName').eq(DEFAULT_DUMMY_USER)
    response = table.query(KeyConditionExpression=filtering_exp)
    crate = response['Items'][0]
    crate_name = crate['CrateName']
    video_list = crate['VideoList']
    print('<div id="default_crate">')
    print(f'<h3 id="crate_name">{crate_name}</h3>')
    print('<ul>')
    for video in video_list:
        print('<li>')
        path = ' '.join(str(key) for key in video.keys())
        print(path.split('\\')[-1])
        print('</li>')
    print('</ul>')
    print('</div>')


def main():
    os.environ['AWS_PROFILE'] = "default"
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
    ddb = resource('dynamodb')
    table = ddb.Table('Crates')
    display_default_crate(table)
#

if __name__ == '__main__':
    main()

