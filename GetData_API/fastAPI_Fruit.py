from fastapi import FastAPI
import pandas

app = FastAPI()
# reading the CSV file

df = pandas.read_csv('fruit.csv')

# displaying the contents of the CSV file
# print(df)
# in ra dong 1 cot 1
# print(csvFile.iloc[0,0])
# in ra dong 1 cot 2
# print(csvFile.iloc[0,1])
# lay index
# print(csvFile[csvFile['fruit'] == "xoai"].index.values)
# Lay Gia tri
# print(df.query('price==10')['fruit'].values)


print(df.loc[df['price'] == 10, 'fruit'].item())

def getPrice(name:str):
    return df.loc[df['fruit'] == name.lower(), 'price'].item()

@app.get("/fruitPrice/")
def price_endpoint(name:str):
    return{"Price of {}:".format(name): getPrice(name)}


