import json
from sqsHandler import SqsHandler


def enviarParaSQSHandler(event, context):
    sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/693632926521/espera-entrega')
    print("event: {}".format(json.dumps(event)))
    return True