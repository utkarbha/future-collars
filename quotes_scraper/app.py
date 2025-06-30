from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import random

Base = declarative_base()
engine = create_engine('sqlite:///quotes.db')
Session = sessionmaker(bind=engine)

class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    author = Column(String)
    tags = Column(String)

Base.metadata.create_all(engine)

def scrape_quotes(min_quotes=100):
    session = Session()
    base_url = 'https://quotes.toscrape.com/page/{}/'
    headers = {"User-Agent": "Mozilla/5.0"}

    total_quotes = session.query(Quote).count()
    page = 1

    while total_quotes < min_quotes:
        print(f"Scraping page {page}...")
        response = requests.get(base_url.format(page), headers=headers)
        if response.status_code != 200:
            print(f"Failed to load page {page}, stopping.")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.select('.quote')
        if not quotes:
            print(f"No quotes found on page {page}, stopping.")
            break

        new_quotes = 0
        for q in quotes:
            text = q.select_one('.text').get_text(strip=True)
            author = q.select_one('.author').get_text(strip=True)
            tags = ', '.join(tag.get_text(strip=True) for tag in q.select('.tags .tag'))

            exists = session.query(Quote).filter_by(text=text).first()
            if not exists:
                session.add(Quote(text=text, author=author, tags=tags))
                new_quotes += 1

        session.commit()
        total_quotes += new_quotes
        print(f"Added {new_quotes} new quotes, total now {total_quotes}")

        if new_quotes == 0:

            break

        page += 1

    session.close()
    print("Scraping complete.")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    search = request.args.get('search', '').strip()
    filter_by = request.args.get('filter_by', 'text')  # default to text
    session = Session()

    if search:
        if filter_by == 'tag':
            quotes = session.query(Quote).filter(Quote.tags.ilike(f'%{search}%')).all()
        else:
            quotes = session.query(Quote).filter(
                (Quote.text.ilike(f'%{search}%')) | (Quote.author.ilike(f'%{search}%'))
            ).all()
    else:
        quotes = session.query(Quote).all()

    session.close()
    return render_template('index.html', quotes=quotes, search=search, filter_by=filter_by)

@app.route('/random')
def random_quote():
    session = Session()
    quotes = session.query(Quote).all()
    session.close()

    if quotes:
        quote = random.choice(quotes)
        return render_template('random.html', quote=quote)
    else:
        return "No quotes available", 404

if __name__ == '__main__':
    scrape_quotes()
    app.run(debug=True)

