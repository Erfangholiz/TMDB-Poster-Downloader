import requests
import os
import tkinter as tk
import ttkbootstrap as ttk 
from tkinter import messagebox

def set_API_key():
    API_file = open('./API_key.txt', 'w')
    API_key = API_entry_StringVar.get()
    API_file.write(API_key)
    API_file.close()
    API_button_StringVar.set('Saved!')


def download():
    status_label_StringVar.set('')
    root.update()
    
    API_KEY = API_entry_StringVar.get()
    movie_id = ID_entry_StringVar.get()
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={API_KEY}"


    response = requests.get(url)
    
    if response.status_code != 200:
        status_label_StringVar.set('Error ' + str(response.status_code) + ", Please make sure you've entered the right information!")
    else:
        text = response.json()
        a = 0
        b = 0
        del text["id"]
        size = []
        for category in text:
            size.append(len(text[f"{category}"]))
        for category in text:
            status_label_StringVar.set(category)
            root.update()
            os.makedirs(f"./Images/{category}", exist_ok = True)
            for image in text[f"{category}"]:
                if root.winfo_viewable():
                    img_url = "https://image.tmdb.org/t/p/w1280" + image["file_path"]
                    img_data = requests.get(img_url).content
                    with open(f'Images/{category}/{str(image["width"])}x{str(image["height"])} {category} ({str(a)}).jpg', 'wb') as handler:
                        handler.write(img_data)
                    progress_label_StringVar.set(str(a + 1) + f'/{str(size[b])} Downloaded')
                    root.update()
                    a += 1
                else:
                    exit()
            a = 0
            b += 1
    status_label_StringVar.set('Finished!')


root = tk.Tk()
root.title('TMDB-Poster-Downloader')
root.geometry('400x200')                

# API inputs
API_input_frame = ttk.Frame(master = root)
API_label = ttk.Label(master = API_input_frame, text = 'API key:')
API_entry_StringVar = tk.StringVar()
if os.path.exists('API_key.txt'):
    API_key_txt = open('API_key.txt', 'r')
    API_key = API_key_txt.read()
    API_entry_StringVar.set(API_key)
API_entry = ttk.Entry(master = API_input_frame, textvariable = API_entry_StringVar)
API_button_StringVar = tk.StringVar()
API_button_StringVar.set('Save')
API_button = ttk.Button(master = API_input_frame, textvariable = API_button_StringVar, command = set_API_key)
API_label.pack(side = 'left')
API_entry.pack(side = 'left', padx = 10)
API_button.pack(side = 'left')
API_input_frame.pack(pady = 20)


# ID inputs
ID_input_frame = ttk.Frame(master = root)
ID_label = ttk.Label(master = ID_input_frame, text = 'Movie ID:')
ID_entry_StringVar = tk.StringVar()
ID_entry = ttk.Entry(master = ID_input_frame, textvariable = ID_entry_StringVar)
ID_button_StringVar = tk.StringVar()
ID_button_StringVar.set('Download')
ID_button = ttk.Button(master = ID_input_frame, textvariable = ID_button_StringVar, command = download)
ID_label.pack(side = 'left')
ID_entry.pack(side = 'left', padx = 10)
ID_button.pack()
ID_input_frame.pack()

#Status
status_label_StringVar = tk.StringVar()
status_label = ttk.Label(master = root, textvariable = status_label_StringVar)
status_label.pack(pady = 10)

#Progress
progress_label_StringVar = tk.StringVar()
progress_label = ttk.Label(master = root, textvariable = progress_label_StringVar)
progress_label.pack()
root.mainloop()

