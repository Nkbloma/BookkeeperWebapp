from webapp import db
from flask_sqlalchemy import SQLAlchemy


class bookrecord_table(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(255))
    book_author = db.Column(db.Integer, db.ForeignKey('author_table.author_id'))
    book_publisher = db.Column(db.Integer, db.ForeignKey('publisher_table.publisher_id'))
    publish_date = db.Column(db.Date)
    start_date = db.Column(db.Date)
    is_finished = db.Column(db.Integer)
    finished_date = db.Column(db.Date)
    number_of_pages = db.Column(db.Integer)
    book_description = db.Column(db.Text)
    current_page = db.Column(db.Integer)
    interest_level = db.Column(db.Integer)
    last_read_date = db.Column(db.Date)

    #Relationships. These are basically how python does joins.
    get_author = db.relationship('author_table', backref='written_books', lazy=True)
    get_publisher = db.relationship('publisher_table', backref='published_books', lazy=True)
    get_genre = db.relationship('genre_table', secondary = 'genrebook_junctiontable')

class author_table(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    author_firstname = db.Column(db.String(255))
    author_lastname = db.Column(db.String(255))

    def __repr__(self):
        return '<Author FirstName: {} \n Author Lastname: {}'.format(self.author_firstname, self.author_lastname)

class publisher_table(db.Model):
    publisher_id = db.Column(db.Integer, primary_key=True)
    publisher_name = db.Column(db.String(255))

    def __repr__(self):
        return '<Publisher Id: {} \n Publisher name: {}'.format(self.publisher_id, self.publisher_name)

class genre_table(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(255))

    def __repr__(self):
        return '<Genre Id: {} Genre name: {}\n'.format(self.genre_id, self.genre_name)

genrebook_junctiontable = db.Table('genrebook_junctiontable', db.metadata,
    db.Column('genre_junctionid', db.Integer, db.ForeignKey('genre_table.genre_id')),
    db.Column('book_junctionid', db.Integer, db.ForeignKey('bookrecord_table.book_id'))
)