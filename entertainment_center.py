import media
import fresh_tomatoes

guardians_of_the_galaxy = media.Movie("Guardians Of The Galaxy Vol. 2",
                                      "Set to the backdrop of Awesome Mixtape #2, 'Guardians of the Galaxy Vol. 2' continues the team's adventures as they unravel the mystery of Peter Quill's true parentage.",
                                      "http://www.entertainmentbuddha.com/blog/wp-content/uploads/2016/10/guardians-of-the-galaxy-vol-2-poster.jpg",
                                      "https://www.youtube.com/watch?v=pr7tDrwQ3t8")

hunger_games = media.Movie("Hunger Games",
                           "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                           "http://www.blackfilm.com/read/wp-content/uploads/2011/07/The-Hunger-Games-poster-3.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

upside_down = media.Movie("Upside Down",
                         "Adam and Eden fell in love as teens despite the fact that they live on twinned worlds with gravities that pull in opposite directions. Ten years after a forced separation, Adam sets out on a dangerous quest to reconnect with his love.",
                         "http://www.seat42f.com/wp-content/uploads/2013/02/Upside-Down-Movie-Poster.jpg",
                         "https://www.youtube.com/watch?v=0jDY1kAgUFY")

deadpool = media.Movie("Deadpool",
                       "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.",
                       "http://www.flickeringmyth.com/wp-content/uploads/2016/01/Deadpool-poster-2-600x875.jpg",
                       "https://www.youtube.com/watch?v=ZIM1HydF9UA")

favorite_movies = [guardians_of_the_galaxy, hunger_games, upside_down, deadpool]

fresh_tomatoes.open_movies_page(favorite_movies)
