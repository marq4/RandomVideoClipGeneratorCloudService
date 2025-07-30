""" Rename Default Crate. """

import json
import os
import sys

import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key

DEFAULT_DUMMY_USER = 'marq_clickops'
DEFAULT_CRATE_ID = 'mEe84OCO'


def rename_crate(table, new_name: str) -> bool:
    """ For now just overwrite Default Crate's name. """
    response = table.update_item(
            Key = {'UserName': DEFAULT_DUMMY_USER, 'CrateID': DEFAULT_CRATE_ID},
            UpdateExpression = 'set CrateName=:n',
            ExpressionAttributeValues = {':n': new_name},
            ReturnValues='NONE'
               )
    stat = response['ResponseMetadata']['HTTPStatusCode']
    #print(stat) #TMP
    if stat == 200:
        return True
    return False
#



def main():
    new_name = sys.argv[1]
    os.environ['AWS_PROFILE'] = "default"
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
    ddb = resource('dynamodb') 
    table = ddb.Table('Crates')
    rename_crate(table, new_name)
#


if __name__ == '__main__':
    main()

