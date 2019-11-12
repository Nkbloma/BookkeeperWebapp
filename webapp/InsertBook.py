from webapp import db
from webapp.models import bookrecord_table, author_table, genre_table, publisher_table
from webapp.forms import CreateBookForm
from flask import Flask, redirect, flash

class InsertBook:
    
    def __init__(self, EnteredForm):
        self.formData = EnteredForm

    def CheckAuthor(self):
        Firstname = self.formData.authorFirstName_field.data
        Lastname = self.formData.authorLastName_field.data
        #Get Author for name
        author_query=author_table.query.filter_by(author_firstname=Firstname, author_lastname=Lastname).first()
        #Search Query for Author First Name and Author Last Name
        if author_query is None:
            newAuthor=author_table(author_firstname=Firstname, author_lastname=Lastname)
            db.session.add(newAuthor)
            db.session.commit()

        authorID_query=author_table.query.filter_by(author_firstname=Firstname, author_lastname=Lastname).first()
        return authorID_query.author_id
        #If Search=NONE db.session(addNewAuthor) db.commit()
        #   search new author, return newauthor.id
        #Else return search.id

    def CheckPublisher(self):
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

    #def GetGenreIDs():
        #for items in chosenFormGenres
        #   bundleofIDS=get genre id where genre = name
        #genreBookIds = array where (newbookID, each genre id)
        #for entries in genreBookIds
        # db.session(genrebook_junction) db.commit
        #Man this is harder than I thought...
        #And I still got an edit and delete logic to make.  
        # I'm going to worry about this last, but it might be
        # best if I were to just add the newbook first than it's genres after
        # That way I know the ID for the newbook exists.


    #By the way to get these things again you might need self. so make an __init__.
    def InsertToTable(self):
        newbook=bookrecord_table(
        book_title=self.formData.bookTitle_field.data,
        book_author=self.CheckAuthor(),
        book_publisher=self.CheckPublisher(),
        publish_date=self.formData.publishedDate_field.data,
        start_date=self.formData.startDate_field.data,
        is_finished=self.CheckisFinished(),
        finished_date=self.formData.finishedDate_field.data,
        number_of_pages=self.formData.pageNumber_field.data,
        book_description=self.formData.bookDescription_field.data,
        current_page=self.formData.currentPage_field.data,
        interest_level=self.formData.interestLevel_field.data
        )
        db.session.add(newbook)
        db.session.commit()
        flash("Book title {}".format(self.formData.bookTitle_field.data))
    """
        Book Title:
            Enter Book title
        
        Book Author: 
            See if Author's name is in the thing. If it is enter id of author
            If not add new author. I don't like the idea that people can just add
            new authors willy nilly, I think it would be best if it worked like genre
            where they're already put in there. This is okay though.

        Book Publisher:
            Same with publisher, I don't like the idea that they can just add publishers
            but I'll deal with it.
        
        Publish Date: Add date if None put None
        Start Date: Add date if None put None
        Finish Date: Add date if None put None
        Number of Pages: add number
        Current Page: Add number
        IsFinished: If false 0 if true 1
        Book Description Add description
        Interest Level: Get number and add it.

        Genre: I'm assuming I just have to get the name, get the ids of the name
        Then add a combination of the new book id and the genre ids into the
        genrejunction table.
    """