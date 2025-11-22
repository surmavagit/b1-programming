print("Welcome to Music Library Manager!")
songs = []
genre_count = {}


def ask_for_song(song_number):
    print(f"Enter Song {song_number}:")
    song_name = input("Song name:")
    song_genre = input("\nGenre:")
    songs.append((song_name, song_genre))
    if song_genre in genre_count:
        genre_count[song_genre] += 1
    else:
        genre_count[song_genre] = 1

    song_number += 1
    print("")


def ask_for_input():
    total_number_of_songs = 5
    song_number = 1
    while song_number <= total_number_of_songs:
        ask_for_song(song_number)
        song_number = song_number + 1


def print_music_library():
    print("=== YOUR MUSIC LIBRARY ===")
    for i, song in enumerate(songs):
        print(f"{i+1}. {song[0]} ({song[1]})")


def print_genre_stats():
    print("=== GENRE STATISTICS ===")
    most_popular = ('', 0)
    for g in genre_count:
        print(f"{g}: {genre_count[g]} song{plural_form(genre_count[g])}")
        if genre_count[g] > most_popular[1]:
            most_popular = (g, genre_count[g])

    print(f"Most popular genre: {most_popular[0]}")


def plural_form(number):
    if number != 1:
        return "s"
    return ""


ask_for_input()
print_music_library()
print_genre_stats()
