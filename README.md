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


## Example

Say we want to check when the next eastbound 14 bus to Davisville Station will be passing by.

<img src="https://user-images.githubusercontent.com/54679389/162833533-b58d68bd-0efa-4dbb-a058-92b123915cb8.png" alt="drawing" width="200"/>

In Agencies/ttc/stop_list.csv, we can see that the TTC stop **Chaplin Crescent at Duncannon Drive, East Side** has the stop_id **3408**.

So we query:

	https://1hifvt9l7e.execute-api.ca-central-1.amazonaws.com/test/pullBusRealtimePredictions?agency=ttc&stop_id=3408

And the API returns:
	
	{
		“agency”: “ttc”, 
		“stop_id”: “3408”,
		“routes”: [
				{
				    “route_id”: “14”,
				    “headsign”: “East - 14 Glencairn towards Davisville Station”,
				    “arrival_pred_mins”: [15, 37, 58]
				}
			   ]
	}

Now we can post in our mapping application that **the next eastbound 14 bus is predicted in 15 minutes**, with another one coming in 37 minutes and then in 58 minutes.
