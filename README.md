# CurbIQ Live Transit Predictions API

## Input

Request using the following URL:

	https://1hifvt9l7e.execute-api.ca-central-1.amazonaws.com/test/pullBusRealtimePredictions?agency={AGENCY}&stop_id={STOP_ID}

- Replace {AGENCY} with one of the standard agency strings (e.g. ‘ttc’)

- Replace {STOP_ID} with the stop_id associated with the stop you are querying

## Output

The output of this request is a JSON of the following format:

	{
		“agency”: “agency name”, 
		“stop_id”: “stop id”,
		“routes”: [
				{
				    “route_id”: “route1 number”,
				    “headsign”: “route1 long name”,
				    “arrival_pred_mins”: [pred1, pred2, pred3, ...]
				},
				{
				    “route_id”: “route2 number”,
				    “headsign”: “route2 long name”,
				    “arrival_pred_mins”: [pred1, pred2, pred3, ...]
				},
				...
			   ]
	}

It lists all routes that service the queried stop, and lists the arrival predictions for the route, in minutes until arrival at the stop.

If a route is not running at the time of query (e.g. if the stop is serviced by a night bus), the “arrival_pred_mins” field will contain an empty array.


