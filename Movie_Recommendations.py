#10 genres, 5 movies each

#welcome message
#input beginning of genre or input all to view all genres
#show choices of genre or all genres
#input genre of choice, ask if want to go back
#once genre is selected, display movies in genre
#ask if want to view other genres, if no, end code

genres = ["Action", "Adventure", "Animation", "Comedy", "Drama", "Fantasy", "Horror", "Science-Fiction", "Thriller", "Western"]
movies = {"Action": ["\nName: Spider-Man: Into the Spider-Verse\nRuntime: 1h 57min\nRating: 4.4/5", "\nName: Inception\nRuntime: 2h 28min\nRating: 4.2/5\n"], 
"Adventure": ["\nName: Spider-Man: No Way Home\nRuntime: 2h 28min\nRating: 4.0/5", "\nName: Everything Everywhere All at Once\nRuntime: 2h 19min\nRating: 4.4/5\n"], 
"Animation": ["\nName: Spirited Away\nRuntime: 2h 5min\nRating: 4.5/5", "\nName: Soul\nRuntime: 1h 41min\nRating: 4.0/5\n"], 
"Comedy": ["\nName: Parasite\nRuntime: 2h 13min\nRating: 4.6/5", "\nName: Fight Club\nRuntime: 2h 19min\nRating: 4.3/5\n"], 
"Drama": ["\nName: Joker\nRuntime: 2h 2min\nRating: 3.9/5", "\nName: Midsommar\nRuntime: 2h 27min\nRating: 3.8/5\n"], 
"Fantasy": ["\nName: The Lighthouse\nRuntime: 1h 49min\nRating: 4.0/5", "\nName: Thor: Ragnarok\nRuntime: 2h 11min\nRating: 3.9/5\n"], 
"Horror": ["\nName: Get Out\nRuntime: 1h 44min\nRating: 4.2/5", "\nName: The Shining\nRuntime: 2h 24min\nRating: 4.3/5\n"], 
"Science-Fiction": ["\nName: Interstellar\nRuntime: 2h 49min\nRating: 4.3/5", "\nName: Dune\nRuntime: 2h 35min\nRating: 4.0/5\n"], 
"Thriller": ["\nName: The Batman\nRuntime: 2h 57min\nRating: 4.1/5", "\nName: Pulp Fiction\nRuntime: 2h 34min\nRating: 4.3/5\n"], 
"Western": ["\nName: Django Unchained\nRuntime: 2h 45min\nRating: 4.2/5", "\nName: The Revenant\nRuntime: 2h 37min\nRating: 3.8/5\n"]}


print("Welcome to Furqan's Movie Emporium!\n\nWhat genre of movie would you like to watch?\n")

def first_input():
    for genre in genres:
        print(genre)
    second_input()

def second_input():
    genre_selection = input("\nPlease input the genre of movie that you would like to watch from the selection above.\n")
    if genre_selection.title() in movies.keys():
        print("\nFurqan's Movie Emporium recommends the following movies under your chosen genre:\n")
        for movie in movies[genre_selection.title()]:
            print(movie)
        third_input()
    else:
        second_input_a()
        
def second_input_a():
    view_again = input("You have entered an invalid genre. Would you like to view the list of genres again? Enter 'y' or 'n' to proceed.\n")
    if view_again == "y":
        first_input()
    elif view_again == "n":
        second_input()
    else:
        print("\nInvalid entry. Please try again.")
        second_input_a()

def third_input():
    third_choice = input("Are you satisifed with your recommendations? Enter 'y' or 'n' to proceed.\n")
    if third_choice == "y":
        print("\nThank you for coming to Furqan's Movie Emporium. Enjoy your movie and have a wonderful day!\n")
    elif third_choice == "n":
        fourth_input()
    else:
        print("\nInvalid entry. Please try again.")
        third_input()

def fourth_input():
    fourth_choice = input("\nWe're sorry to hear that. Would you like to try again? Enter 'y' or 'n' to proceed.\n")
    if fourth_choice == "y":
        first_input()
    elif fourth_choice == "n":
        print("\nThank you for coming to Furqan's Movie Emporium. Have a wonderful day!")
    else:
        print("\nInvalid entry. Please try again.")
        fourth_input()

first_input()






