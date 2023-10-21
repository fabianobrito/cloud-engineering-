import json
import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO


dao = BaseDAO('eventos-pizzaria')


def gravaEventosHandler(event, context):
    detail = event['detail']
    dao.put_item({'pedido':detail['pedido']),
        'status':detail['status'],
        'cliente':detail['cliente'],
        'time':str(datetime.now())})
    return True