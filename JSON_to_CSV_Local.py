import requests
import csv

def main():

    ## Specify API endpoint
    res = requests.get("https://www.tablebuilder.singstat.gov.sg/publicfacing/api/json/title/14885.json")

    ## Raise exception if API request unsuccessful
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")

    ## Store API response
    data = res.json()

    ## Extract only "Level3"
    subset = data["Level3"]

    ## Write to CSV, with three headers - "date", "country", "value"
    with open("result.csv", "w") as csvfile:

        f = csv.writer(csvfile)

        f.writerow(["date", "country", "value"])

        for i in subset:
            f.writerow([i["month"], i["level_3"], i["value"]])

if __name__ == "__main__":
    main()
