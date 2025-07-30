""" Save list of dictionaries to DDB table and return it. """

import json
import os
import sys

import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key

DEFAULT_DUMMY_USER = 'marq_clickops'
DEFAULT_CRATE_ID = 'mEe84OCO'


#def get_crate_from_ddb(user: str, crate_name: str) -> list:
#    """ Returns list of (video_title, duration) pairs. """
#    pass


def persist_default_crate(crate: list, table) -> bool:
    """ For now just overwrite Default Crate. """
    response = table.update_item(
            Key = {'UserName': DEFAULT_DUMMY_USER, 'CrateID': DEFAULT_CRATE_ID},
            UpdateExpression = 'set VideoList=:v',
            ExpressionAttributeValues = {':v': crate},
            ReturnValues="UPDATED_NEW"
               )
    stat = response['ResponseMetadata']['HTTPStatusCode']
    #print(stat) #TMP
    if stat == 200:
        return True
    return False
#



def read_json(filename: str) -> list:
    """ Imports and returns pairs from json. """
    loaded_data = ''
    with open(filename, 'r', encoding='utf-8') as file:
        json_str = file.read()
    loaded_data = json.loads(json_str)
    return loaded_data
#

def display_default_crate(table) -> None:
    """ Prints HTML of the Default crate & default dummy 'user' from DDB. """
    filtering_exp = Key('UserName').eq(DEFAULT_DUMMY_USER)
    response = table.query(KeyConditionExpression=filtering_exp)
    print(response)



def main():
    """ Read JSON from disk, parse it, store crate to DDB. """
    filename = sys.argv[1]
    pairs = read_json(filename)
    #display_as_unorderedlist(pairs)
    os.environ['AWS_PROFILE'] = "default"
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
    ddb = resource('dynamodb') 
    table = ddb.Table('Crates')
    if persist_default_crate(pairs, table):
        print("<h3>Default crate overwritten!</h3>")
        display_default_crate(table)
    else:
        print("<h3>There was a problem storing the crate to the DB!</h3>")
#


if __name__ == '__main__':
    main()

