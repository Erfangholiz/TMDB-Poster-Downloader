import requests
import os
import tkinter as tk

root = tk.Tk()


API_KEY = input ('Enter TMDB API key: ')
movie_id = input('Enter movie_id: ')
url = f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={API_KEY}"


response = requests.get(url)
text = response.json()
a = 0
del text["id"]
size = 0
for category in text:
    size += len(text[f"{category}"])
for category in text:
    os.makedirs(f"./Images/{category}", exist_ok = True)
    for image in text[f"{category}"]:
        img_url = "https://image.tmdb.org/t/p/w1280" + image["file_path"]
        img_data = requests.get(img_url).content
        with open(f'Images/{category}/{str(image["width"])}x{str(image["height"])} {category} ({str(a)}).jpg', 'wb') as handler:
            handler.write(img_data)
        a += 1

