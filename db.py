from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.iagram
#collection = db.iagram
collection = db.iagram_weekly3

def RamdomQuote():
    #q = collection.find(query)
    q=collection.aggregate([{ "$sample": { "size": 1 }}])
    for q in q:
        frase=(q['Frase'])
        autor=(q['Autor'])
    return frase,autor

def QuotebyId(id):
    q=collection.find_one({"_id": ObjectId(id)})
    frase=(q['Frase'])
    autor=(q['Autor'])
    return frase,autor


def GetQuotesList():
    q=collection.find({})
    return q
