from flask import Flask, jsonify, request

playlist = [{1:{"Name": "One"}}, {2:{"Name": "Two"}}, {3:{"Name": "Three"}}, {4:{"Name": "Four"}}]

# # for song in playlist:
# #     for key, value in song.items():
# #         for name, data in value.items():
# #             print(data)

# # print(list(playlist[0].values())[0]["Name"])
# # print (list(playlist[0].values())[0])

# # for song in playlist:
# #     print(list(song.values())[0]["Name"])

    

def merge_sort(playlist):
    if len(playlist) > 1:
        mid = len(playlist)//2
        left_half = playlist[:mid]
        right_half = playlist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

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
            
    return playlist

def search(song_list, name):
    merge_sort(song_list)
    low = 0
    high = len(song_list) -1

    while low <= high:
        mid = (low + high) // 2
        if list(song_list[mid].values())[0]["Name"] == name:
            return (f"Song {name} found.")
        elif list(song_list[mid].values())[0]["Name"] < name:
            low = mid + 1
        else:
            high = mid - 1

    return (f"Song '{name}' not found.")

print(merge_sort(playlist))
print(search(playlist, "Three"))