from pymongo import MongoClient
from bson.json_util import dumps
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.iagram
collection = db.iagram

def RamdomQuote():
    #q = collection.find(query)
    q=collection.aggregate([{ "$sample": { "size": 1 }}])
    for q in q:
        frase=(q['Frase'])
        autor=(q['Autor'])
    return frase,autor

frase,autor=RamdomQuote()
