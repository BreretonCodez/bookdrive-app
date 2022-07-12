import click
import csv
from flask import Flask
from App import create_db, db, app, Book


@app.cli.command("init")
def initialize():
    create_db(app)

    with open('books.csv') as csvfile:
      reader = csv.reader(csvfile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)

      next(reader, None)
      
      for row in reader:
        book = Book(isbn=row[0].strip('"'), title=row[1].strip('"'), author=row[2].strip('"'), publication_year=row[3].strip('"'), publisher=row[4].strip('"'))
        db.session.add(book)
      db.session.commit()
  
    print('database intialized')
