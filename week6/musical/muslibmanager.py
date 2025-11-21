print("Welcome to Music Library Manager!")
songs = []
genre_count = {}

def ask_for_song(song_number):
    print(f"Enter Song {song_number}:")
    song_name = input("Song name:")
    song_genre = input("\nGenre:")
    song_number = song_number + 1
    print("")

def ask_for_input():
    total_number_of_songs = 5
    song_number = 1
    while song_number <= total_number_of_songs:
        ask_for_song(song_number)
        song_number = song_number + 1

ask_for_input()
