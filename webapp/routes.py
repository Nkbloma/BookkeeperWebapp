from webapp import app
from flask import Flask, redirect, flash, render_template, url_for
from webapp import db
from webapp.models import bookrecord_table, author_table, genre_table, publisher_table #genrebook_junctiontable
from webapp.forms import CreateBookForm
from webapp.InsertBook import InsertBook

@app.route('/')
@app.route('/records')
def records():
    Book = bookrecord_table.query.all()
    return render_template("index.html", title="records", books = Book)

@app.route('/bookrecord/<thisBooksTitle>')
def bookrecord(thisBooksTitle):
    thisBooksRecords = bookrecord_table.query.filter_by(book_title = thisBooksTitle).first()

    thisBooksAuthor = thisBooksRecords.get_author
    thisBooksPublisher = thisBooksRecords.get_publisher.publisher_name
    thisBooksPublishDate = thisBooksRecords.publish_date
    thisBooksGenres = thisBooksRecords.get_genre
    thisBooksInterestLevel = thisBooksRecords.interest_level
    thisBooksStartDate = thisBooksRecords.start_date
    thisBooksCurrentPage = thisBooksRecords.current_page
    thisBooksPageLength = thisBooksRecords.number_of_pages
    thisBooksIsFinished = thisBooksRecords.is_finished
    thisBooksFinishDate = thisBooksRecords.finished_date
    thisBooksDescription = thisBooksRecords.book_description
    thisBooksLastReadDate = thisBooksRecords.last_read_date

    return render_template("bookrecord.html", 
    Title = thisBooksTitle,
    Author = thisBooksAuthor.author_firstname + ' ' + thisBooksAuthor.author_lastname,
    Publisher = thisBooksPublisher,
    PublishDate = thisBooksPublishDate,
    Genres = thisBooksGenres,
    InterestLevel = thisBooksInterestLevel,
    StartDate = thisBooksStartDate,
    CurrentPage = thisBooksCurrentPage,
    PageLength = thisBooksPageLength,
    IsFinished = thisBooksIsFinished,
    FinishDate = thisBooksFinishDate,
    Description = thisBooksDescription,
    LastReadDate = thisBooksLastReadDate
    )

@app.route('/createbook', methods=['GET', 'POST'])
def createbook():
    createForm = CreateBookForm()
    if createForm.validate_on_submit():
        formInstance=InsertBook(createForm)
        formInstance.InsertToTable()
        return redirect('/records')

    return render_template("createbook.html", title="createbook", form=createForm)

@app.route('/info')
def info():
    return render_template("index.html", title="info")