import requests
import json


# fetch data from json url
def fetch_data(url):
    try:
        # to make a get request from the url
        response = requests.get(url)

        # check the request was successful
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            # error handling if response has bad request
            print(f"Failed to fetch data: {response.status_code}")
            return None
    except Exception as e:
        print(f"Failed to fetch data: {str(e)}")
        return None


# parse the json data
def parse_data(data):
    if data:
        # Extract time updated
        time_updated = data['time']['updated']

        # Extract GBP rate
        currency = input("Currency:")
        gbp_rate = data['bpi'][currency]['rate']

        # Display information
        print(f"Time Updated: {time_updated}")
        print(f"GBP Rate: {gbp_rate}")


def main():
    # Input API endpoint
    url = input("url:")

    # fetch data from API
    bpi_data = fetch_data(url)

    # Parse information
    parse_data(bpi_data)


if __name__ == "__main__":
    main()
