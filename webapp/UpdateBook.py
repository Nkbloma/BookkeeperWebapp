from webapp import db
from webapp.models import *
from webapp.forms import BookForm
from flask import Flask, redirect, flash
from sqlalchemy import and_

class UpdateBook:
    ListOfGenreIds = []
    def __init__(self, EnteredForm, EnteredBook):
        self.formData = EnteredForm
        self.bookData = EnteredBook
        EnteredAuthor = author_table.query.filter_by(author_id=self.bookData.book_author).first()
        EnteredPublisher = publisher_table.query.filter_by(publisher_id=self.bookData.book_author).first()
        EnteredGenres = bookrecord_table.query.filter_by(book_id=self.bookData.book_id).first().get_genre

        for genre in EnteredGenres:
            self.ListOfGenreIds.append(genre.genre_id)
        


    def CheckAuthorExists(self):
        Firstname = self.formData.authorFirstName_field.data
        Lastname = self.formData.authorLastName_field.data
        author_query=author_table.query.filter_by(author_firstname=Firstname, author_lastname=Lastname).first()
        if author_query is None:
            newAuthor=author_table(author_firstname=Firstname, author_lastname=Lastname)
            db.session.add(newAuthor)
            db.session.commit()

        authorID_query=author_table.query.filter_by(author_firstname=Firstname, author_lastname=Lastname).first()
        return authorID_query.author_id
        #If Search=NONE db.session(addNewAuthor) db.commit()
        #   search new author, return newauthor.id
        #Else return search.id

    def CheckPublisherExists(self):
        PublisherName=self.formData.publisherName_field.data

        #Get Author for name
        publisher_query=publisher_table.query.filter_by(publisher_name=PublisherName).first()
        #Search Query for Author First Name and Author Last Name
        if publisher_query==None:
            newPublisher=publisher_table(publisher_name=PublisherName)
            db.session.add(newPublisher)
            db.session.commit()

        publisherID_query=publisher_table.query.filter_by(publisher_name=PublisherName).first()
        return publisherID_query.publisher_id
        #Get Publisher for name
        #Search Query for Publisher Name
        #If Search=NONE db.session(addNewPublisher) db.commit()
        #   search newpublisher return newpublisher.id
        #Else return search.id

    def CheckisFinished(self):
        formFinished = self.formData.isFinished_field.data
        if not formFinished:
            return 0
        else:
            return 1
        #If formFinished = false return 0
        #Else return 1.
    
    def DeleteUpdateGenreIDs(self):
        #Get genre ids from bookrecord and use them to delete them from junction.
        gen = genrebook_junctiontable
        genreDeleteCommand = genrebook_junctiontable.delete().where(genrebook_junctiontable.c.book_junctionid == self.bookData.book_id)
        db.session.execute(genreDeleteCommand)
        db.session.commit()
        #Gets genre ids from form data and enters them into junction
        arrayofIds = []
        formGenres = self.formData.genreType_field.data
        for genre in formGenres:
            arrayofIds.append(int(genre))
        
        for id in arrayofIds:
            db.session.execute(genrebook_junctiontable.insert().values(genre_junctionid=id, book_junctionid=self.bookData.book_id))
       
        db.session.commit()


    #By the way to get these things again you might need self. so make an __init__.'''
    def UpdateTable(self):
        self.bookData.book_title=self.formData.bookTitle_field.data,
        self.bookData.book_author=self.CheckAuthorExists(),
        self.bookData.book_publisher=self.CheckPublisherExists(),
        self.bookData.publish_date=self.formData.publishedDate_field.data,
        self.bookData.start_date=self.formData.startDate_field.data,
        self.bookData.last_read_date=self.formData.lastRead_field.data,
        self.bookData.is_finished=self.CheckisFinished(),
        self.bookData.finished_date=self.formData.finishedDate_field.data,
        self.bookData.number_of_pages=self.formData.pageNumber_field.data,
        self.bookData.book_description=self.formData.bookDescription_field.data,
        self.bookData.current_page=self.formData.currentPage_field.data,
        self.bookData.interest_level=self.formData.interestLevel_field.data

        db.session.commit()
        self.DeleteUpdateGenreIDs()
        #The id needs to be created first
        flash("Book title {} Genres{}".format(self.formData.bookTitle_field.data, self.formData.genreType_field.data))
 