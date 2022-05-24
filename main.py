import pymongo
from fastapi import FastAPI
import json
from mongoengine import connect
from bson import json_util

#from venv.zegarki_scraper.zegarki_scraper.start import odpal



app = FastAPI()
username = 'koledzy_projekt'
password = 'u1mkLXkE4niiONPd'
connect(db='zegarki',host='cluster0.hwii5.mongodb.net', port=27017, username=username, password=password)

client = pymongo.MongoClient("mongodb+srv://koledzy_projekt:u1mkLXkE4niiONPd@cluster0.hwii5.mongodb.net/test")
db = client['zegarki']


@app.get("/")
def dane():

    return ("TEST")
def parse_json(data):
    return json.loads(json_util.dumps(data))
@app.get("/pokazDane")
async def ShowEuroData():

   table = db["scrapy_items"]
   data = list(parse_json(table.find({})))
   return data
'''
@app.get("/aktualizujDane")
def aktualizuj():
    odpal.scrapy_to_db()
    return ("DANE ZAKTUALIZOWANE")
    '''

