import api.utils as utils
import api.providers.oxtorrent as oxtorrent
from flask import Flask, render_template, request, url_for, flash, redirect
import urllib.parse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search/', methods=['GET'])
def search():
    args = request.args
    query = args.get('query')
    results = oxtorrent.searchTorrents(query)
    
    return render_template("search.html", results=results)

@app.route('/view/', methods=['GET'])
def view():
    args = request.args
    source = args.get('source')
    magnet = oxtorrent.getMagnet(urllib.parse.unquote(source))
    return render_template("view.html", magnet=magnet)
    
  

if __name__=='__main__': 
   app.run(debug=True) 