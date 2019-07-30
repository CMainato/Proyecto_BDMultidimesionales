#pip install couchdb
#pip install tweepy

import couchdb #Libreria de CouchDB (requiere ser instalada primero)
from tweepy import Stream #tweepy es la libreria que trae tweets desde la API de Twitter (requiere ser instalada primero)
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json #Libreria para manejar archivos JSON


ckey = "eKMoXznT1M6jvJpJaxR0Bj6fk"
csecret = "ApqsAUPaFYM4csDpaDYqBnkZD1arHSP5w4e9juU6aRU3Ki1xMR"
atoken = "1136022577938391041-BoYBWezAYgHtOT1gK3fAzvWN9qmFvD"
asecret = "slkksvHM8UnhJX3aXNvvreAo6BTx1cYbJr1cuUF18RR44"

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
           
            doc = db.save(dictTweet) #Aqui se guarda el tweet en la base de couchDB
            print ("Guardado " + "=> " + dictTweet["_id"])
        except:
            print ("Documento ya existe")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

#Setear la URL del servidor de couchDB
server = couchdb.Server('http://localhost:5984/')
try:
    #Si no existe la Base de datos la crea
    db = server.create('newyork')
except:
    #Caso contrario solo conectarse a la base existente
    db = server['newyork']
    
#Aqui se define el bounding box con los limites geograficos donde recolectar los tweets
twitterStream.filter(locations=[-79.63,40.83,-73.22,45.42])
