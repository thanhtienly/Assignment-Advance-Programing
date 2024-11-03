from fastapi import FastAPI
from csv_reader import CSV_Reader
import json
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/query')
def get_transactions(amount: str = "", message : str = "", page: int = 1):
    
    with open('index.json', 'r') as file:
        indexes = json.load(file)

    csvReader = CSV_Reader()
    try:
        [min_offset, max_offset] = indexes[amount]
    except:
        min_offset = 0
        max_offset = indexes['max_offset']

    result = csvReader.filter_transaction_with_message('./sorted_transactions.csv', message, page, min_offset, max_offset)

    return result
