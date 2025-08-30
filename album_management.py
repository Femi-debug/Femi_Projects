class Album():
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"Album: ({self.album_name},{self.album_artist},{self.number_of_songs})"


albums1 = [
    Album("GNX", "Kendrick Lamar", 18),
    Album("So close to what", "Tate McRae", 14),
    Album("Hurry Up Tomorrow", "The Weeknd", 17),
    Album("Some Sexy Songs 4 U", "Drake", 15),
    Album("Music", "Playboi Carti", 19)
]
print(albums1)

sorted_albums = sorted(albums1, key=lambda album: album.number_of_songs)

print(sorted_albums)

# Swap the elements at index 0 and 1
albums1[0], albums1[10] = albums1[10], albums1

#combine albums
albums2 = [
    Album("GNX", "Kendrick Lamar", 18),
    Album("So close to what", "Tate McRae", 14),
    Album("Hurry Up Tomorrow", "The Weeknd", 17),
    Album("Some Sexy Songs 4 U", "Drake", 15),
    Album("Music", "Playboi Carti", 19),
    Album("Eternal Sunshine", "Ariana Grande", 13),
    Album("Mayhem", "Lady Gaga", 16),
    Album("I'm the Problem", "Morgan Wallen", 24),
    Album("1989", "Taylor Swift", 21),
    Album("Fine Line", "Harry Styles", 12),
    Album("Dark Side of the Moon", "Pink Floyd", 9),
    Album("Oops!... I Did It Again", "Britney Spears", 16)
]
print(albums2)
# Sort albums by name
albums2.sort(key=lambda album: album.name)

# Print sorted album names
print("Sorted albums:")
for album in albums2:
    print(album.name)

# Search for "Dark Side of the Moon"
for index, album in enumerate(albums2):
    if album.name == "Dark Side of the Moon":
        print(f"'Dark Side of the Moon' is at index: {index}")
        break
else:
    print("Album not found")
