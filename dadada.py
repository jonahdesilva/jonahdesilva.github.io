import os

with open("dada.txt", "a") as f:
    for file in os.listdir("media/photos"):
        f.write(f"""
        <figure class="gallery-item">
            <img src="media/photos/{file}">
        </figure>
        """)
