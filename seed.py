from app import create_app, db
from app.models.book import Book

my_app = create_app()
with my_app.app_context():
    db.session.add(Book(title="You become what you think", year=2023, description="Self improvement")),
    db.session.add(Book(title="Harry Potter and sorcerer's stone", year=1998, description="Children's book")),
    db.session.add(Book(title="The book thief", year=2007, description="Children's book")),
    db.session.add(Book(title="The silent patient", year=2019, description="Thriller")),
    db.session.add(Book(title="In five years", year=2020, description="Fantasy")),
    db.session.add(Book(title="The secret of elephants", year=2022, description="Finction")),
    db.session.add(Book(title="The keeper of happy Endings", year=2021, description="Fiction")),
    db.session.add(Book(title="The diary of a wimpy kid:hot mess", year=2024, description="Children's book")),
    db.session.add(Book(title="The great Gatsby", year=1925, description="Fiction")),
    db.session.add(Book(title="Lord of the rings", year=2012, description="Fantasy")),
    
    db.session.commit()