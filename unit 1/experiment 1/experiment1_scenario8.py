class Movie:
    def __init__(self, name, rating, ticket_price):
        self.name = name
        self.rating = rating
        self.ticket_price = ticket_price

    def get_category(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"

    def display(self):
        print("Movie Name:", self.name)
        print("Rating:", self.rating)
        print("Ticket Price:", self.ticket_price)
        print("Category:", self.get_category())
        print("------------------------")


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\nMovie Details")
        print("========================")
        for movie in self.movies:
            movie.display()

cinema = Cinema()

n = int(input("Enter number of movies: "))

for i in range(n):
    print("\nEnter details of Movie", i + 1)
    name = input("Movie Name: ")
    rating = float(input("Rating (out of 10): "))
    ticket_price = float(input("Ticket Price: "))

    m = Movie(name, rating, ticket_price)
    cinema.add_movie(m)

cinema.display_movies()