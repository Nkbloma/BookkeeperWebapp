from webapp import db
from flask_sqlalchemy import SQLAlchemy

class bookrecord_table(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(255))
    author = db.Column(db.Integer, db.ForeignKey('author_table.author_id'))
    book_publisher = db.Column(db.Integer, db.ForeignKey('publisher_table.publisher_id'))
    publish_date = db.Column(db.Date)
    start_date = db.Column(db.Date)
    is_finished = db.Column(db.Integer)
    start_page = db.Column(db.Integer)
    last_page = db.Column(db.Integer)
    book_description = db.Column(db.Text)
    current_page = db.Column(db.Integer)

    def __repr__(self):
        return '<Bookrecord_Model {}>'.format(self.book_title)

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