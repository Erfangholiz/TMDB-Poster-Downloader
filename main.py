import requests
import os
import tkinter as tk
import ttkbootstrap as ttk 

#Saves the API so there's no need to enter it every time.
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
    #The url provided by TMDB for retrieving movie images, https://developer.themoviedb.org/reference/movie-images
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={API_KEY}"

    response = requests.get(url)
    
    if response.status_code != 200:
        status_label_StringVar.set('Error ' + str(response.status_code) + ", Please make sure you've entered the right information!")
    else:
        #Using a JSON format for the response so it's easier to sift through
        text = response.json()
        
        #An integer to keep track of the names of the files, 2000x3000 Poster (img_number)
        img_number = 1
        
        #An integer to keep track of the number of files to be downloaded in each category (Backdrops, Logos, Posters)
        category_number = 0
        
        #Deleting the "id" key from the JSON response because it would mess up the for loop as it's numeric and can't be iterated.
        del text["id"]
        
        #Storing the size of every category and making directories
        size = []
        for category in text:
            size.append(len(text[f"{category}"]))
            os.makedirs(f"./Images/{category.title()}", exist_ok = True)
            
        for category in text:
            status_label_StringVar.set(category.title())
            for image in text[f"{category}"]:
                #Checks every iteration to see if the user has closed the window so it can stop running the script if so
                if root.winfo_viewable():
                    img_url = "https://image.tmdb.org/t/p/original" + image["file_path"]
                    img_extension = image["file_path"].split('.')[1]
                    img_data = requests.get(img_url).content
                    #Saving the image in this format: widthxheight Category (img_number).img_extension
                    # In the Images/Category/ subdirectory
                    with open(f'Images/{category.title()}/{str(image["width"])}x{str(image["height"])} {category.title()[0:-1]} ({str(img_number)}).{img_extension}', 'wb') as handler:
                        handler.write(img_data)
                    progress_label_StringVar.set(str(img_number) + f'/{str(size[category_number])} Downloaded')
                    root.update()
                    img_number += 1
                else:
                    #If the window has been closed, the program gets killed
                    exit()
            img_number = 1
            category_number += 1
        status_label_StringVar.set('Finished!')
        progress_label_StringVar.set(f'{str(sum(size))}/{str(sum(size))} Downloaded')
        root.update()


#Root definition
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

