import json
import requests
import urllib2
import datorama

## Specify API endpoint, make a request call and store JSON response
response = urllib2.urlopen('https://www.tablebuilder.singstat.gov.sg/publicfacing/api/json/title/14885.json')
data = json.load(response)

## Extract only "Level3"
subset = data["Level3"]

## Write header row
header = ["date", "country", "value"]
datorama.add_row(header)

## Write data rows
for i in subset:
	datorama.add_row([i["month"], i["level_3"], i["value"]])

## Write result to CSV and push to data stream
datorama.save()
