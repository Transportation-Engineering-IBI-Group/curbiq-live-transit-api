import requests as rq
import xmltodict
import json

def pull_RTPI(event, context):
    
    print(event)
    # parse out query string parameters:
    
    def pull_RTPI_NextBus(agency,stop_id):
        
        stop_url = 'https://retro.umoiq.com/service/publicXMLFeed?command=predictions&a={AGENCY}&stopId={STOP}'.format(AGENCY=agency,STOP=stop_id)
        response = rq.get(stop_url)
        resp_dict = xmltodict.parse(response.content)
        
        next_arrival_resp = dict()
        next_arrival_resp['agency'] = agency
        next_arrival_resp['stop_id'] = stop_id
        
        next_arrival_resp['routes'] = []
        
        routes = [route['@routeTag'] for route in resp_dict['body']['predictions']]
        
        for i,route in enumerate(routes):
            next_arrival_resp['routes'].extend([dict()])
            next_arrival_resp['routes'][i]['route_id'] = route
            next_arrival_resp['routes'][i]['headsign'] = resp_dict['body']['predictions'][0]['direction'][i]['@title']
            next_arrival_resp['routes'][i]['arrival_pred_mins'] = [int(pred['@minutes']) for pred in resp_dict['body']['predictions'][0]['direction'][i]['prediction']]
            
        return next_arrival_resp
    
    def pull_RTPI_GTFSrt(agency,stop_id):
        
        next_arrival_resp = dict()

        return next_arrival_resp
        
        
    agency = event['queryStringParameters']['agency']
    stop_id = event['queryStringParameters']['stop_id']
    
    nextbus_agencies = ['ttc']
    gtfs_rt_agencies = ['mbta']
    
    if agency in nextbus_agencies:
        
        next_arrival_response = pull_RTPI_NextBus(agency,stop_id)
        
    elif agency in gtfs_rt_agencies:
        
        next_arrival_response = pull_RTPI_GTFSrt(agency,stop_id)

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {},
        "multiValueHeaders": {},
        "body": json.dumps(next_arrival_response)
    }

with open('lambda-sourcecode-function/test_event.json', 'r') as f:
    event = json.load(f)

pull_RTPI(event, '')