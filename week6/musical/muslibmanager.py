print("Welcome to Music Library Manager!")
songs = []
genre_count = {}

def ask_for_song(song_number):
    print(f"Enter Song {song_number}:")
    song_name = input("Song name:")
    song_genre = input("\nGenre:")
    song_number = song_number + 1
    songs.append({ 'name': song_name, 'genre': song_genre })

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
    for i in range(len(songs)):
        print(f"{i+1}. {songs[i]['name']} ({songs[i]['genre']})")
    print("=== GENRE STATISTICS ===")
    most_popular_genre = [0,"none"]
    for genre in genre_count:
        print(f"{genre}: {genre_count[genre]} songs")
        if genre_count[genre] > most_popular_genre[0]:
            most_popular_genre[0] = genre_count[genre]
            most_popular_genre[1] = genre

    print(f"Most popular genre: {most_popular_genre[1]}")


ask_for_input()
print_report()
