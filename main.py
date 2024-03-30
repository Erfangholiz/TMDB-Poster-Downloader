import requests
import os
import tkinter as tk
import ttkbootstrap as ttk 

def set_API_key():
    API_file = open('./API_key.txt', 'w')
    API_key = API_entry_StringVar.get()
    API_file.write(API_key)
    API_file.close()

# API_KEY = input ('Enter TMDB API key: ')
# movie_id = input('Enter movie_id: ')
# url = f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={API_KEY}"


# response = requests.get(url)
# text = response.json()
# a = 0
# del text["id"]
# size = 0
# for category in text:
#     size += len(text[f"{category}"])
# for category in text:
#     os.makedirs(f"./Images/{category}", exist_ok = True)
#     for image in text[f"{category}"]:
#         img_url = "https://image.tmdb.org/t/p/w1280" + image["file_path"]
#         img_data = requests.get(img_url).content
#         with open(f'Images/{category}/{str(image["width"])}x{str(image["height"])} {category} ({str(a)}).jpg', 'wb') as handler:
#             handler.write(img_data)
#         a += 1


root = tk.Tk()
root.title('TMDB-Poster-Downloader')
root.geometry('400x200')

API_entry_StringVar = tk.StringVar()
API_entry_StringVar.set('blah')

input_frame = ttk.Frame(master = root)
API_label = ttk.Label(master = input_frame, text = 'API key:')
API_entry = ttk.Entry(master = input_frame, textvariable = API_entry_StringVar)
API_button = ttk.Button(master = input_frame, text = 'Confirm', command = set_API_key)
API_label.pack(side = 'left')
API_entry.pack(side = 'left', padx = 10)
API_button.pack(side = 'left')
input_frame.pack(pady = 20)

root.mainloop()

