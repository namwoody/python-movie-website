
import fresh_tomatoes

import media

sardaarji = media.Movie('Sardaar ji','Actor in this movie diljit','http://static.blugaa.com/thumbs/100_100/mivvi.png','https://www.youtube.com/watch?v=Y93uXRGGEN8')

sultan = media.Movie('sultan','Salman Khan movie','http://s1.dmcdn.net/VvYWv.jpg','https://www.youtube.com/watch?v=wPxqcq6Byq0')

grandmasti = media.Movie('grand masti','Vivek oberio movie','https://upload.wikimedia.org/wikipedia/en/f/fa/Grand_Masti.jpg','https://www.youtube.com/watch?v=ZojV0FC-KdI')

udtapunjab = media.Movie('udta punjab','shahid kapoor','https://1.bp.blogspot.com/-ZsFINk-jOss/VrcXKqAyrdI/AAAAAAAAPDI/NkfKXRBqq5s/s1600/udta-punjab-movies-story-and-script-are-the-real-heroes.JPG','https://www.youtube.com/watch?v=EJylz_9KYf8')

lovepunjab = media.Movie('love punjab','amrinder','http://t1.gstatic.com/images?q=tbn:ANd9GcSaR-Zp1mbXvzizHotmUggUDRuKxwVpdE6VhTiAxjqIQfpkdzK0','https://www.youtube.com/watch?v=1lTWvdYxUMk')

dishoom = media.Movie('Dishoom','John Ambrahim','https://i.ytimg.com/vi/DU6IdS2gVog/maxresdefault.jpg','https://www.youtube.com/watch?v=DU6IdS2gVog')

#print(action.storyline)

#junglebook.show_trailer()
#action.show_trailer()
movies = [sardaarji,sultan,grandmasti,udtapunjab,lovepunjab,dishoom]
fresh_tomatoes.open_movies_page(movies)