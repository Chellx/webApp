from flask import Flask, render_template, request

# from <module> import <class>

app = Flask(__name__)


@app.route("/")
def display_homepage():
    return render_template(
        "homepage.html",
        the_title="Welcome to My Website",
        the_opening_title="Welcome to My Website",
    )


@app.route("/personalInfo")
def display_personalInfo():
    return render_template(
        "personalInfo.html",
        the_title="About Me",
        the_opening_title="Read all about me",
    )


@app.route("/cv")
def display_cv():
    return render_template(
        "cv.html",
        the_title="My CV",
        the_opening_title="Here you can read all about my work experience and educational background",
    )


@app.route("/processform", methods=["POST"])
def process_form_data():
    data = request.form
    with open("comments.txt", "a") as VisitorComments:
        print(data["theemail"], ",", sep="", end="", file=VisitorComments)
        print(data["thecomment"], file=VisitorComments)
        VisitorComments.write("\n")
    return render_template(
        "thanks.html",
        the_title="Thank you!",
        the_opening_title="Thanks for your comment",
    )


@app.route("/faveTech")
def display_faveTech():
    return render_template(
        "faveTech.html",
        the_title="Favourite Tech",
        the_opening_title="Some Of My Favourite Computing Things",
    )


@app.route("/timeular")
def display_timeular():
    return render_template(
        "timeular.html", the_title="Timeular", the_opening_title="Timeular",
    )


@app.route("/playdate")
def display_playdate():
    return render_template(
        "playdate.html", the_title="Playdate", the_opening_title="Playdate",
    )


@app.route("/ringo")
def display_ringo():
    return render_template("ringo.html", the_title="Ringo", the_opening_title="Ringo",)


@app.route("/hobbies")
def display_hobbies():
    return render_template(
        "hobbies.html", the_title="Hobbies", the_opening_title="My Hobbies",
    )
