import fresh_tomatoes
# fresh_tomatoes is a module given by udacity for getting the required output with all HTML and css style guides
import media
#media is module where we have defined the class movie
toy_story = media.Movie("Toy story",
                        "A story of a boy and his toy that comes to his life",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
Avatar = media.Movie("Avatar",
                     "Story of marine in alien world",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
Hidden_figures= media.Movie("hidden figures",
                            "The Story of the women behind great mission",
                            "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg",
                            "https://www.youtube.com/watch?v=RK8xHq6dfAo")
                            
The_help= media.Movie("the help",
                      "Change begins with whisper",
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcTrqv4Be3lT75Ez3uzgUPuCOtFkGML6IDL0n5Ea6eSmiSXQeBt2",
                      "https://www.youtube.com/watch?v=l0dWCXCjX9o")
game_of_thrones=media.Movie("GOT",
                            "Winter is coming",
                            "https://images-na.ssl-images-amazon.com/images/I/81IXojwauiL.jpg",
                            "https://www.youtube.com/watch?v=giYeaKsXnsI")
Inside_out=media.Movie("Inside out",
                       "Meet the little voices in your head",
                       "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",
                       "https://www.youtube.com/watch?v=seMwpP0yeu4")
movies = [toy_story,Avatar,Hidden_figures,The_help,game_of_thrones,Inside_out]
#defining the Array/list of movie names which is the input for open movies page function
fresh_tomatoes.open_movies_page(movies)
#calling the class open_movies_page which is inside the fresh tomatoes module
