# CurbIQ Live Transit Predictions API

## Input

Request using the following URL:
https://1hifvt9l7e.execute-api.ca-central-1.amazonaws.com/test/pullBusRealtimePredictions?agency={**AGENCY**}&stop_id={**STOP_ID**}
•	Replace {AGENCY} with one of the standard agency strings (e.g. ‘ttc’)
•	Replace {STOP_ID} with the stop_id associated with the stop you are querying

## Output

The output of this request is a JSON of the following format:

{
      “agency”: “agency name”, 
      “stop_id”: “stop id”,
      “routes”: [
                  {
                      “route_id”: “_route1 number_”,
                      “headsign”: “_route1 long name_”,
                      “arrival_pred_mins”: [_pred1, pred2, pred3, ..._]
                  },
                  {
                      “route_id”: “_route2 number_”,
                      “headsign”: “_route2 long name_”,
                      “arrival_pred_mins”: [_pred1, pred2, pred3, ..._]
                  },
                  ...
               ]
}

It lists all routes that service the queried stop, and lists the arrival predictions for the route, in minutes until arrival at the stop.
If a route is not running at the time of query (e.g. if the stop is serviced by a night bus), the “arrival_pred_mins” field will contain an empty array.


