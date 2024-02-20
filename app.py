import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

@app.route('/albums', methods=['POST'])
def post_album():
    if has_invalid_album_parameters(request.form):
        return 'You need to submit a title, release_year and artist_id', 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, 
                request.form['title'],
                request.form['release_year'],
                request.form['artist_id'])
    repository.create(album)
    return '', 200

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return '\n'.join(f'{album}' for album in repository.all())

def has_invalid_album_parameters(form):
    return 'title' not in form or 'release_year' not in form or 'artist_id' not in form
# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

