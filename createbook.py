from webapp import db
from webapp.models import bookrecord_table

newbook=bookrecord_table(
    book_title='BOBLUSbook',
    book_author=1,
    book_publisher=2,
    publish_date='2011-1-1',
    start_date=None,
    is_finished=0,
    finished_date=None,
    number_of_pages=125,
    book_description="Tis a new book",
    current_page=0,
    interest_level=2
)
db.session.add(newbook)
db.session.commit()