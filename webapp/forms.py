from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from webapp.models import genre_table

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class CreateBookForm(FlaskForm):
    genres= genre_table.query.all()
    genreChoices=[]
    for x in genres:
        genreChoices.append((str(x.genre_id), x.genre_name))

    bookTitle_field = StringField('Book Title')
    authorFirstName_field = StringField('Author First Name')
    authorLastName_field = StringField('Author Last Name')
    publisherName_field = StringField('Publisher Name')
    publishedDate_field = DateField('Published Date')
    genreType_field = MultiCheckboxField('Genre Type', choices=genreChoices)
    startDate_field = DateField('Start Date')
    currentPage_field = IntegerField('Current Page')
    lastRead_field = DateField('Last Time Read')
    isFinished_field = BooleanField('Finished')
    finishedDate_field = DateField('Finished Date')
    pageNumber_field = IntegerField('Number of Pages')
    bookDescription_field = TextAreaField('Description')
    interestLevel_field = RadioField('Interest Level', choices=[
        ('1', 'None'),
        ('2', 'Meh'),
        ('3', 'Mild'),
        ('4', 'Above'),
        ('5', 'High')
        ]
    )
    submit_field = SubmitField('Submit')