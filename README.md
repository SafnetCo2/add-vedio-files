## Flask Video Application
A clean and simple CRUD web application built using Flask, HTML, and CSS, demonstrating how to create, read, update, and delete video records stored in a local JSON file.
This project is ideal for learning or showcasing Flask fundamentals, template rendering, and basic full-stack logic.
## Features

 Create: Add new videos with a title and author

 Read: View all uploaded videos

 Update: Edit video details directly on the page

 Delete: Remove videos instantly

Persistent Storage: Saves data locally in a videos.json file (no database required)
## Create virtual Enviroment
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or
.venv\Scripts\activate      # Windows
## Install Dependencies
pip install flask
## Run application
python3 app.py
## in Browser
Visit: 👉 http://127.0.0.1:5000
 ## How It Works

The app maintains a list of videos using an in-memory structure that syncs to a JSON file.

Each time a user performs a CRUD operation, the JSON file is updated accordingly.

Flask’s templating system (Jinja2) renders all the video entries dynamically.

The layout is kept minimal, responsive, and clean with plain CSS for simplicity.
## Technologies used
| Layer      | Technology                                     |
| ---------- | ---------------------------------------------- |
| Backend    | Flask (Python)                                 |
| Frontend   | HTML5, CSS3                                    |
| Storage    | JSON File                                      |
| Templating | Jinja2                                         |
| Deployment | Localhost (can easily extend to Render/Heroku) |


## Future Enhancements

 Add support for video URLs or file uploads

Include comments under each video

Implement a search or filter feature

Migrate from JSON to a relational database (MySQL or PostgreSQL)

Improve UI with Bootstrap or React frontend

##  Author

Josephine Nzioka
🎓 Bachelor of Business Management | Junior Software Developer
 Based in Kenya | 🌍 Open to Remote Internships
 [kimmyjmueni@gmail.com]

## License

This project is licensed under the MIT License[License]
 — free to use, modify, and distribute.
