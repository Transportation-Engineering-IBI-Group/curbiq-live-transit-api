import requests as rq
import xmltodict
import json

def pull_RTPI(event, context):
    
    # parse out query string parameters:
    
    def pull_RTPI_NextBus(agency,stop_id):
        
        stop_url = 'https://retro.umoiq.com/service/publicXMLFeed?command=predictions&a={AGENCY}&stopId={STOP}'.format(AGENCY=agency,STOP=stop_id)
        response = rq.get(stop_url)
        resp_dict = xmltodict.parse(response.content)
        
        next_arrival_resp = dict()
        next_arrival_resp['agency'] = agency
        next_arrival_resp['stop_id'] = stop_id
        
        next_arrival_resp['routes'] = []
        
        if type(resp_dict['body']['predictions']) != list:
            routes = [resp_dict['body']['predictions']]
        else:
            routes = [route for route in resp_dict['body']['predictions']]
    
        i = 0
        for route in routes:
            if 'direction' in route:
                direction = route['direction']
                if type(direction)==list:
                    for subdir in direction:
                        next_arrival_resp['routes'].extend([dict()])
                        next_arrival_resp['routes'][i]['route_id'] = subdir['@title'].split(' - ')[1].split(' ')[0]
                        next_arrival_resp['routes'][i]['headsign'] = subdir['@title']
                        if type(subdir['prediction'])==list:
                            next_arrival_resp['routes'][i]['arrival_pred_mins'] = [int(pred['@minutes']) for pred in subdir['prediction']]
                        else:
                            next_arrival_resp['routes'][i]['arrival_pred_mins'] = [int(subdir['prediction']['@minutes'])]
                        i+=1
                else:
                    next_arrival_resp['routes'].extend([dict()])
                    next_arrival_resp['routes'][i]['route_id'] = route['@routeTag']
                    next_arrival_resp['routes'][i]['headsign'] = direction['@title']
                    if type(direction['prediction'])==list:
                        next_arrival_resp['routes'][i]['arrival_pred_mins'] = [int(pred['@minutes']) for pred in direction['prediction']]
                    else:
                        next_arrival_resp['routes'][i]['arrival_pred_mins'] = [int(direction['prediction']['@minutes'])]
                    i+=1
            else:
                next_arrival_resp['routes'].extend([dict()])
                next_arrival_resp['routes'][i]['route_id'] = route['@routeTag']
                next_arrival_resp['routes'][i]['headsign'] = route['@dirTitleBecauseNoPredictions']
                next_arrival_resp['routes'][i]['arrival_pred_mins'] = []
                i+=1
        
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
