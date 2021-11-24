from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


# ----------- Age/Gender guess API ------------- #
def guess_age(name):
    response = requests.get(url=f"https://api.agify.io/?name={name}")
    response.raise_for_status()
    data = response.json()
    if data['count'] == 0:
        return "Ageless!"
    else:
        return str(data['age'])


def guess_gender(name):
    response = requests.get(url=f"https://api.genderize.io/?name={name}")
    response.raise_for_status()
    data = response.json()
    if data['count'] == 0:
        return "Attack helicopter"
    else:
        return str(data['gender'])


# ----------- Flask code ------------ #
@app.route('/')
def home():
    curr_year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=curr_year)


@app.route('/guess/<name>')
def guess(name):
    age = guess_age(name)
    gender = guess_gender(name)
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/88292704844daa394f39"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)