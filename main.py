import json


from flask import Flask, render_template, request


DATA_FILE = "metacritic.json"



def get_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    


all_data = get_data()


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/lol")
def lol():
    return render_template("lol.html")


@app.route("/tg")
def tg():
    return render_template("tg.html")


@app.route("/games")
def games():
    PAGINATOR_SIZE = request.args.get("limit", 8, type=int)
    
    page = request.args.get("page", 1, type=int)
    if page < 1 or page > len(all_data)//PAGINATOR_SIZE + 1 :
        page = 1
    
    paginator = {
        "next": page + 1,
        "prev": page - 1,
        "current": page,
        "total": len(all_data)//PAGINATOR_SIZE + 1,
        "limit": PAGINATOR_SIZE,
    }
    list_games = all_data[(page - 1) * PAGINATOR_SIZE : page * PAGINATOR_SIZE]
    
    return render_template("games.html", data=list_games, paginator=paginator)

if __name__ == "__main__":
    app.run(debug=True, port=8000)