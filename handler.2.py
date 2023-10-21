import json

    
def entreguesHandler(event, context):
    print("event: {}".format(json.dumps(event)))
    return True