""" Remove all videos from default crate by default user. """

import os
import boto3
#from boto3 import resource
#from boto3.dynamodb.conditions import Attr, Key

DEFAULT_DUMMY_USER = 'marq_clickops'
DEFAULT_CRATE_ID = 'mEe84OCO'


def empty_crate(user_name: str, crate_id: str, ddb):
    """ Remove all videos from crate and commit to DDB. """
    response = ddb.update_item(
            TableName='Crates',
            Key={
                'UserName': {'S': user_name},
                'CrateID': {'S': crate_id}
                },
            UpdateExpression="SET VideoList = :empty_list",
            ExpressionAttributeValues={
                ':empty_list': {'L': []}
                                      },
            ReturnValues='NONE'
    )
    #print('<p>Crate emptied.</p>', \
    #        response['ResponseMetadata']['HTTPStatusCode'] == 200)
#


def main():
    os.environ['AWS_PROFILE'] = "default"
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
    ddb = boto3.client('dynamodb')
    #table = ddb.Table('Crates')
    empty_crate(DEFAULT_DUMMY_USER, DEFAULT_CRATE_ID, ddb)
#

if __name__ == '__main__':
    main()


