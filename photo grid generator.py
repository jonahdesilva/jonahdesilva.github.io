import os
import random

with open("photogrid generator result.txt", "a", encoding="utf-8") as file:
    filenames = os.listdir("media/photos")
    random.shuffle(filenames)
    for filename in filenames:
        file.write(f'''
        <figure class="gallery-item">
            <img src="media/photos/{filename}">
        </figure>
        ''')