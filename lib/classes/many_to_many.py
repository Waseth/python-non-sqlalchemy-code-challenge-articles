class Article:
    all = []  # Class attribute to keep track of all articles

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)  # Append the newly created article to the list

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author class.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")
        self._magazine = value



class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        topics = set()
        for article in self._articles:
            topics.add(article.magazine.category)
        return list(topics) if topics else None

    def contributing_magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article



class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = []
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        for author, count in author_counts.items():
            if count > 2:
                authors.append(author)
        return authors if authors else None

    def top_publisher(self):
        magazine_counts = {}
        for article in self._articles:
            magazine = article.magazine
            if magazine in magazine_counts:
                magazine_counts[magazine] += 1
            else:
                magazine_counts[magazine] = 1
        if magazine_counts:
            return max(magazine_counts, key=magazine_counts.get)
        else:
            return None
