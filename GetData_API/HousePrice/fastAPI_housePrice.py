from fastapi import FastAPI
from fastapi import Response
import pandas

app = FastAPI()

df = pandas.read_csv('house-prices.csv')
df.sort_values('Price')
# print(df.sort_values('Price'))

# print(df[(df['Price'] < 100000) & (df['Price'] > 80000) & (df['Neighborhood'] == 'North')].sort_values('Price'))


def getHouse_List(lowest_price,highest_price,neighbor):
    return df[(df['Price'] <= highest_price) & (df['Price'] >= lowest_price) & (df['Neighborhood'] == neighbor.capitalize())].sort_values('Price')



@app.get("/housePrice/")
def housePrice_endpoint(lowest_price:int, highest_price:int,neighbor:str):
    list = getHouse_List(lowest_price, highest_price, neighbor)
    return Response(list.to_json(orient="records"), media_type="application/json")

