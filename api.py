from fastapi import FastAPI, HTTPException
import requests
import simplejson

app = FastAPI()

# Endpoint GET
@app.get("/api")
def get_data():
    return {"data": "Este es el dato"}

# Endpoint POST
@app.post("/api")
def fetch_external_api():
    try:
        response = requests.get("https://api.publicapis.org")
        response.raise_for_status()  # Raise an HTTPError for bad responses

        if "application/json" in response.headers.get("content-type", ""):
            data = response.json()
            print("Response from external API:", data)
            return data
        else:
            print("HTML Response from external API:", response.text)
            return response.text
        
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching external API: {str(e)}")
    except simplejson.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Error decoding JSON: {str(e)}")
    
# Endpoint UPDATE
@app.put("/api/{number}")
def square_number(number: int):
    result = number ** 2
    return {"result": result}
    