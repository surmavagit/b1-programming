print("Welcome to Music Library Manager!")
songs = []
genre_count = {}

def ask_for_song(song_number):
    print(f"Enter Song {song_number}:")
    song_name = input("Song name:")
    song_genre = input("\nGenre:")
    song_number = song_number + 1
    songs.append((song_name, song_genre))

    if song_genre in genre_count:
        genre_count[song_genre] += 1
    else:
        genre_count[song_genre] = 1

    print("")

def ask_for_input():
    total_number_of_songs = 5
    song_number = 1
    while song_number <= total_number_of_songs:
        ask_for_song(song_number)
        song_number = song_number + 1

def print_report():
    print("=== YOUR MUSIC LIBRARY ===")
    counter = 1
    for song_name, song_genre in songs:
        print(f"{counter}. {song_name} ({song_genre})")
        counter += 1

    print("=== GENRE STATISTICS ===")
    for gen_name, gen_number in genre_count.items():
        print(f"{gen_name}: {gen_number} songs")

    print(f"Most popular genre: {max(genre_count, key=genre_count.get)}")


ask_for_input()
print_report()
