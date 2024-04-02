<img src="TMDB-Poster-Downloader-Logo.png">
<h1 align = "center">TMDB-Poster-Downloader</h1>
<p align = "center">A simple program written in python that recieves a TMDB API key and a movie ID and downloads all of the images available on the website.</p>

## Use cases
- Backdrops can be used in reviews and analyses relevant to the movie they're about (e.g. I used one that I found on TMDB for <a href="https://medium.com/@erfan1382gh/a-complete-breakdown-of-annette-2021-from-start-to-finish-8b7c28e39d94">my analysis on Annette (2021)</a>).

- Logos can be indispensable for video essayists especially because a lot of the ones provided by TMDB have transparent backgrounds which makes them great for thumbnails.

- Posters can be a great encapsulation of the marketing techniques used in the industry at the time, they can also give you great contrast when compared to posters from other countries which are sometimes also provided on the website.

Posters and backdrops can be a very neat thing for all movie enthusiasts.

## How to Use:
- First, you need to acquire a TMDB API key, there are a couple of guides available online. Overall creating an account and getting the key should take less than five minutes.
- Download the latest version or just clone the source as shown below:
  
        git clone https://github.com/Erfangholiz/TMDB-Poster-Downloader.git

        cd TMDB-Poster-Downloader/
        
        python main.py

- And the rest is pretty self-explanatory, enter the API key and click save (this step is only required on first-time use or if your key stopped working) and then copy the movie ID from the URL. For example this is the URL for Slaughterhouse-Five (1972):

        https://www.themoviedb.org/movie/24559-slaughterhouse-five

- And this is the Movie ID:
  
        24559-slaughterhouse-five