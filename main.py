from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Base, Book


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_books = db.session.query(Book).all()

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        new_book = Book(title=title, author=author, rating=rating)
        new_book.save()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get("id")
    book_to_edit = db.session.query(Book).get(book_id)

    if request.method == "POST":
        book_to_edit.rating = request.form["rating"]
        book_to_edit.save()

        return redirect(url_for("home"))

    return render_template("edit.html", book=book_to_edit)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book_to_delete = db.session.query(Book).get(book_id)
    book_to_delete.delete()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
