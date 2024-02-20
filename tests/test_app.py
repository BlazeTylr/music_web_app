"""
When I call POST /albums with album info
I see it in the list in GET /albums
"""

def test_post_albums(db_connection, web_client):
    db_connection.seed('seeds/album_collection.sql')
    post_response = web_client.post('/albums', data={'title': 'Randezvous', 'release_year': '2023', 'artist_id': '2'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == '' \
    'Album(1, Imagine, 1978, 1)\n' \
    'Album(2, Randezvous, 2023, 2)'

"""
When I call get /albums, I'll get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/album_collection.sql")
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '' \
    'Album(1, Imagine, 1978, 1)'

def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed('seeds/album_collection.sql')
    post_response = web_client.post('/albums')
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == 'You need to submit a title, release_year and artist_id'

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == '' \
    'Album(1, Imagine, 1978, 1)'


# POST /albums
# title: 'Randezvous'
# release_year: 2023
# artist_id: 2
#  Expected response (200 OK):
"""
(no content)
"""

# GET /albums
#  Expected response (200 OK):
"""
Album (1, 'Imagine', 1978, 1)
Album (2, 'Randesvouz', 2023, 1)
"""

# POST /albums
#  Expected response (400 Bad Request):
"""
(no content)
"""

# GET /albums
#  Expected response (200 OK):
"""
Album (1, 'Imagine', 1978, 1)
"""