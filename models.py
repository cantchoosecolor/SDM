import datetime


class User:
    """User"""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.collections = []

    def create_collection(self, game):
        self.collections.append(game)

    def write_post(self, title, description):
        return Post(title, description)

    def write_comment(self, post, text):
        comment = Comment(text)
        post.add_comment(comment)
        return comment


class Game:
    """PC game model."""
    def __init__(self, title, release_date, description, developer, processor,
                 graphics_card, operating_system):
        self.title = title
        self.release_date = release_date
        self.description = description
        self.developer = developer
        self.processor = processor
        self.graphics_card = graphics_card
        self.operating_system = operating_system


class Developer:
    """Developer."""
    def __init__(self, name):
        self.name = name


class Processor:
    """Processor."""
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


class GraphicsCard:
    """Graphics Card."""
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


class OperatingSystem:
    """Operating System."""
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


class Post:
    """Posts."""
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.date = datetime.datetime.now()
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)


class Comment:
    """Post comments."""
    def __init__(self, text):
        self.text = text
        self.date = datetime.datetime.now()


class Collection:
    """User Collection."""
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def remove_game(self, game):
        self.games.remove(game)


class GameSearch:
    def __init__(self):
        super().__int__()
        self.genre_model = Genre
        self.graphic_model = GraphicCard
        self.os_model = Os
        self.processor_model = Processor



