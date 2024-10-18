from flask import Flask, jsonify, request
from functions import merge_sort


app = Flask(__name__)

songs = [] # this will hold dictionaries of songs.  They will have ID: then a dictionary for Name: and Genre:

playlists = {}

song_id = 0


@app.route('/show_songs', methods=['GET'])
def show_songs():
    song_list = []
    for song in songs:
        for song_id, details in song.items():
            song_list.append({
                "ID": song_id,
                "Name": details['Name'],
                "Genre": details['Genre'],
                "Artist": details['Artist']
            })
    return jsonify(song_list), 200

@app.route('/show_by_genre/<string:genre>', methods=['GET'])
def show_by_genre(genre):
    song_list = []
    for song in songs:
        for song_id, details in song.items():
            if details['Genre'] == genre:
                song_list.append({
                    "ID": song_id,
                    "Name": details['Name'],
                    "Genre": details['Genre'],
                    "Artist": details['Artist']
                })
    return jsonify(song_list), 200

@app.route('/show_by_name/<string:name>', methods=['GET'])
def search(name):
    merge_sort(songs)
    low = 0
    high = len(songs) -1

    while low <= high:
        mid = (low + high) // 2
        if list(songs[mid].values())[0]["Name"] == name:
            return jsonify(f"Song '{name}' found."), 200
        elif list(songs[mid].values())[0]["Name"] < name:
            low = mid + 1
        else:
            high = mid - 1

    return jsonify(f"Song '{name}' not found."), 404


@app.route('/add_song', methods=['POST'])
def add_song():
    global song_id
    song_id += 1
    data = request.get_json()
    if not data:
        return jsonify({"error": "No song provided."}), 400
    
    songs.append({song_id: {'Name': data['Name'], 'Genre': data['Genre'], 'Artist': data['Artist']}})
    print(songs)
    return jsonify({"message": "Song added succesfully."}), 200


@app.route('/update_song/<int:id>', methods=['PUT'])
def update_song():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No song provided."}), 400
    
    for song in songs:
        for song_id, details in song.items():
            if song_id == id:
                song = ({song_id: {'Name': data['Name'], 'Genre': data['Genre'], 'Artist': data['Artist']}})
                print(songs)

    return jsonify({"message": "Song added succesfully."}), 200



@app.route('/delete_song/<int:id>', methods=['DELETE'])
def delete_song(id):
    for song in songs:
        for song_id, details in song.items():
            if song_id == id:
                songs.remove(song)

    return jsonify({"message": "Song deleted succesfully."}), 200

#  Playlist Routes -------------------------------------------------->

@app.route('/show_playlists', methods=['GET'])
def show_playlists():
    if playlists:
        return jsonify(playlists), 200
    else:
        return jsonify({'message': 'There are no playlists created.'}), 404

@app.route('/show_songs_by_name/<string:playlist_name>', methods=['GET'])
def get_playlist_name(playlist_name):
    playlist = playlists[playlist_name]
    return merge_sort_name(playlist)

def merge_sort_name(playlist):

    if len(playlist) > 1:
        mid = len(playlist)//2
        left_half = playlist[:mid]
        right_half = playlist[mid:]

        merge_sort_name(left_half)
        merge_sort_name(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if list(left_half[i].values())[0]["Name"] < list(right_half[j].values())[0]["Name"]:
                playlist[k] = left_half[i]
                i += 1
            else:
                playlist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            playlist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            playlist[k] = right_half[j]
            j += 1
            k += 1
            
    return jsonify(playlist)


@app.route('/show_songs_by_genre/<string:playlist_name>', methods=['GET'])
def get_playlist_genre(playlist_name):
    playlist = playlists[playlist_name]
    return merge_sort_genre(playlist)

def merge_sort_genre(playlist):

    if len(playlist) > 1:
        mid = len(playlist)//2
        left_half = playlist[:mid]
        right_half = playlist[mid:]

        merge_sort_genre(left_half)
        merge_sort_genre(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if list(left_half[i].values())[0]["Genre"] < list(right_half[j].values())[0]["Genre"]:
                playlist[k] = left_half[i]
                i += 1
            else:
                playlist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            playlist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            playlist[k] = right_half[j]
            j += 1
            k += 1
            
    return jsonify(playlist)


@app.route('/show_songs_by_artist/<string:playlist_name>', methods=['GET'])
def get_playlist_artist(playlist_name):
    playlist = playlists[playlist_name]
    return merge_sort_artist(playlist)

def merge_sort_artist(playlist):

    if len(playlist) > 1:
        mid = len(playlist)//2
        left_half = playlist[:mid]
        right_half = playlist[mid:]

        merge_sort_artist(left_half)
        merge_sort_artist(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if list(left_half[i].values())[0]["Artist"] < list(right_half[j].values())[0]["Artist"]:
                playlist[k] = left_half[i]
                i += 1
            else:
                playlist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            playlist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            playlist[k] = right_half[j]
            j += 1
            k += 1
            
    return jsonify(playlist)



@app.route('/add_playlist/<string:name>', methods=['POST'])
def add_playlist(name):
    playlists[name] = []
    return jsonify({"message": "Playlist added succesfully."}), 200

@app.route('/add_song_to_playlist/<string:playlist_name>', methods=['PUT'])
def add_song_to_playlist(playlist_name):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No song provided."}), 400
    
    for song in songs:
        for key, value in song.items():
            if data['Name'] == value['Name']:
                playlists[playlist_name].append({key:value})
    
    return jsonify({"message": "Song added to playlist succesfully."}), 200

@app.route('/delete_song_from_playlist/<string:playlist_name>', methods=['DELETE'])
def delete_song_from_playlist(playlist_name):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No song provided."}), 400
    
    for song in playlists[playlist_name]:
        for key, value in song.items():
            if data['Name'] == value['Name']:
                playlists[playlist_name].remove({key:value})

    return jsonify({"message": "Song deleted from playlist succesfully."}), 200


@app.route('/delete_playlist/<string:name>', methods=['DELETE'])
def delete_playlist(name):
    try:
        del playlists[name]
        return jsonify({"message": "Playlist deleted succesfully."}), 200

    except Exception as e:
        return jsonify({"message": "Error: Playlist not found."}), 404




print(songs)

if __name__ == '__main__':
    app.run(debug=True)