# Import flask, json manipulations, .env, allow cors and functions from search module

from flask import Flask,request,Response
from flask_cors import CORS
import json
from search import search,get_lyrics
import db
from os import getenv
from dotenv import load_dotenv
load_dotenv()


# Initialize flask app
app = Flask(__name__)

# Allow CORS from specific origins
CORS(app)
CORS(app, origins=getenv("CORS").split(","))

# Route for getting songs by query
@app.route('/get-songs')
def get_songs():
    # get query from "..../get-songs?q=<query>"
    query = request.args.to_dict().get("q")

    # if query exists start searching
    if query:
        return Response(
            json.dumps({
                "success":True,
                "message": "List of songs by your query",
                "results": search(query)
            }, ensure_ascii=False
            ), 
        content_type="Application/json"
        )
    
    # if query does not exist return success:false message
    return Response(
        json.dumps({
            "success":False,
            "message":'query parameter "q" is empty or does not exist'
        },ensure_ascii=False
        ),
    content_type="Application/json"
    )


@app.route('/get-passwords')
def get_passwords():

    if True: # make auth check
        return Response(
            json.dumps({
                "success":True,
                "message": "List of all passwords",
                "results": db.get_passwords()
            }, ensure_ascii=False
            ), 
        content_type="Application/json"
        )
    return Response(
        json.dumps({
            "success":False,
            "message":'Wrong session'
        },ensure_ascii=False
        ),
    content_type="Application/json"
    )




if __name__ == '__main__':
  app.run(debug=True)