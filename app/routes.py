from flask import Flask, jsonify
from .connection import ArtstationRepository
app = Flask(__name__)


@app.route('/artist/<id>')
def get_artist(id:str = None):
    repository = ArtstationRepository()
    artist = repository.get_artist(id)
    artist['_id'] = str(artist['_id'])
    return jsonify(artist)

@app.route('/artwork/<id>')
def get_artwork(id:str = None):
    repository = ArtstationRepository()
    artwork = repository.get_artwork(id)
    artwork['_id'] = str(artwork['_id'])
    for comment in artwork['comments']:
        comment['_id'] = str(comment['_id'])
        for nested in comment['nested']:
            nested['_id'] = str(nested['_id'])
    print(artwork)
    return jsonify(artwork)

@app.route('/previews')
def get_previews():
    repository = ArtstationRepository()
    previews = repository.get_previews()
    for preview in previews:
        preview['_id'] = str(preview['_id'])
    return jsonify(previews)








