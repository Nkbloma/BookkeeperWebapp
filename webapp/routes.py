from webapp import app
from flask import Flask, redirect, render_template
from webapp import db
from webapp.models import bookrecord_table, author_table, genre_table, publisher_table, genrebook_junctiontable

@app.route('/')
@app.route('/records')
def records():
    Book = bookrecord_table.query.all()
    
    return render_template("index.html", title="records", books = Book)

@app.route('/bookrecord/<currentTitle>')
def bookrecord(currentTitle):
    CurrentBookRecords = bookrecord_table.query.filter_by(book_title = currentTitle).first()
    currentBookAuthor = author_table.query.filter_by(author_id=CurrentBookRecords.book_author).first()

    return render_template("bookrecord.html", 
    thisTitle=currentTitle,
    thisAuthor = currentBookAuthor.author_firstname + ' ' + currentBookAuthor.author_lastname
    )

@app.route('/createbook')
def createbook():
    return render_template("index.html", title="createbook")

@app.route('/info')
def home():
    return render_template("index.html", title="info")