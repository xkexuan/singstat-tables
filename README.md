# JSON to CSV

This is a simple script written to make an API call to one of SingStat's many [commonly accessed tables](https://www.tablebuilder.singstat.gov.sg/publicfacing/initApiList.action), parse and extract data from the JSON response, and write the output as a .csv file.

## Usage

This script was originally developed to write the JSON response of the International Visitor Arrivals data as a .csv file.

| No. | Subject | Topic | Title | CSV | JSON |
|-----|---------|-------|-------|-----|------|
| 1 |  Tourism | International Visitor Arrivals | [International Visitor Arrivals By Inbound Tourism Markets, Monthly](https://www.tablebuilder.singstat.gov.sg/publicfacing/viewTable.action?titleId=14885) | [CSV](https://www.tablebuilder.singstat.gov.sg/publicfacing/api/csv/title/14885.csv) | [JSON](https://www.tablebuilder.singstat.gov.sg/publicfacing/api/json/title/14885.json)

### Modifications

For usage on other [commonly accessed tables](https://www.tablebuilder.singstat.gov.sg/publicfacing/initApiList.action) available on the SingStat website, modification of the script is required by specifying the unique API endpoint, and also depending on which data elements need to be extracted.

### Versions

Two versions of the script are available.

### For use on local machine or IDE

This version can be executed in the terminal or IDE:
```
python inbound-csv.py
```
The output .csv will be saved in the current working directory.

### For use in Datorama

This version is modified for use in Datorama to automate the ingestion of data into a Datorama data stream. In this version, the output .csv is automatically uploaded to Datorama and will not be stored on the local machine.

To automate data retrieval in Datorama:
1. Specify Frequency (e.g. Daily) and Delivery Hour (e.g. 06)
2. Ensure that "Enable Data Retrieval" is selected
