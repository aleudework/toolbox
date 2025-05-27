import requests

def api_test(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params)
        print("Statuskode:", response.status_code)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Fejl under forespørgsel:", e)
    except ValueError:
        print("Responsen er ikke gyldig JSON.")


def api_json(url, headers=None, params=None):

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
        return response.json()
    
    # Returns exception
    except requests.exceptions.RequestException as e:
        print("Fejl under forespørgsel:", e)
    
    # Returns if value error
    except ValueError:
        print("Responsen er ikke gyldig JSON.")