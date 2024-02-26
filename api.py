from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Endpoint GET
@app.get("/GET")
def get_data():
    return {"data": "Este es el dato"}

# Endpoint POST
@app.post("/POST")
def fetch_external_api():
    try:
        response = requests.get("https://api.publicapis.org")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        print("Response from external API:", data)
        return data
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching external API: {str(e)}")

# Endpoint UPDATE
@app.put("/PUT/{number}")
def square_number(number: int):
    result = number ** 2
    return {"result": result}
    