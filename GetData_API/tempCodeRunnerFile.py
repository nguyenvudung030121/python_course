from fastapi import FastAPI
import pandas

# app = FastAPI()


# reading the CSV file

csvFile = pandas.read_csv('fruit.csv')

# displaying the contents of the CSV file

print(csvFile.iloc[1:0])
