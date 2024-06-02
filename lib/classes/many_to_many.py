class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
            self._articles_written = []
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles_written

    def magazines(self):
        return list({article.magazine for article in self._articles_written})

    def add_article(self, magazine, title):
        for article in self._articles_written:
            if article.magazine == magazine and article.title == title:
                return article


        article = Article(self, magazine, title)
        self._articles_written.append(article)
        return article

    def topic_areas(self):
        areas = set()
        for article in self._articles_written:
            areas.add(article.magazine.category)
        return list(areas) if areas else None

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")

        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")

        self._articles_published = []

        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return self._articles_published

    def contributors(self):
        return list({article.author for article in self._articles_published})

    def article_titles(self):
        if not self._articles_published:
            return None
        return [article.title for article in self._articles_published]

    def contributing_authors(self):
        if not self._articles_published:
            return None

        authors = {}
        for article in self._articles_published:
            author = article.author
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1
        return [author for author, count in authors.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine.articles()))
    
    def topic_areas(self):
        return list(set(article.author.topic_areas() for article in self._articles_published))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")

        author.articles().append(self)
        magazine.articles().append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Author must be of type Author.")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Magazine must be of type Magazine.")
