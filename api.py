import requests
import pandas as pd
import json

def api_test(url, headers=None, params=None):
    """
    Retunerer hele response, kræver at alt er defineret i header for at hente ud.
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        print("Statuskode:", response.status_code)
        return response
    except requests.exceptions.RequestException as e:
        print("Fejl under forespørgsel:", e)
    except ValueError:
        print("Responsen er ikke gyldig JSON.")




def api_json(url, headers=None, params=None, show=True):
    """
    Retunerer array med header og body response i json.
    Sættes show til True, printes output i json format på fanct json metode
    """

    # Creates empty headers if no headers
    if headers is None:
        headers = {}

    # Appends application/json if not a part of headers. 
    if "accept" not in {key.lower() for key in headers}:
        headers["accept"] = "application/json"

    try:
        # Returns a json-object
        response = requests.get(url, headers=headers, params=params)
        print("Statuskode:", response.status_code)

        if show:
            print(json.dumps(response.json(), indent=2))

        return [response.headers, response.json()]
    
    # Returns exception
    except requests.exceptions.RequestException as e:
        print("Fejl under forespørgsel:", e)
    
    # Returns if value error
    except ValueError:
        print("Responsen er ikke gyldig JSON.")


def api_json_to_df(url, headers=None, params=None):

    # Creates empty headers if no headers
    if headers is None:
        headers = {}

    # Appends application/json if not a part of headers. 
    if "accept" not in {key.lower() for key in headers}:
        headers["accept"] = "application/json"


    try:
        # Returns a json-object
        response = requests.get(url, headers=headers, params=params)
        print("Statuskode:", response.status_code)
        json_output = response.json()

        return pd.DataFrame(json_output)

    # Returns exception
    except requests.exceptions.RequestException as e:
        print("Fejl under forespørgsel:", e)
    
    # Returns if value error
    except ValueError:
        print("Responsen er ikke gyldig JSON.")