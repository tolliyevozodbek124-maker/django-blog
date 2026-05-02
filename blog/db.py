import json


DEMO_DB_PATH = "db.json"

class Database:
    def __init__(self, path=DEMO_DB_PATH):
        self.path = path

    def read(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def write(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def get_articles(self):
        data = self.read()
        return data.get("articles", [])
    
    def get_latest_articles(self, count=3):
        articles = self.get_articles()
        return articles[:count]
    
    def get_article_by_slug(self, slug):
        articles = self.get_articles()
        for article in articles:
            if article.get("slug") == slug:
                return article
        return None

    def add_article(self, title, content):
        articles = self.get_articles()
        new_article = {
            "id": len(articles) + 1,
            "title": title,
            "content": content,
            "slug": title.lower().replace(" ", "-")
        }
        articles.append(new_article)
        self.write({"articles": articles})

    def find_articles_by_title(self, q):
        data = self.read()
        articles = []
        for article in data['articles']:
            if q.lower() in article['title'].lower():
                articles.append(article)
        
        return articles
    