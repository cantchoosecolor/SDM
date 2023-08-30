import datetime
from dataclasses import dataclass
import sqlalchemy as sa


class User:
    """User."""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.friends = []


    def create_collection(self, game):
        self.collections.append(game)

    @staticmethod
    def write_post(title, description):
        return Post(title, description)

    @staticmethod
    def write_comment(post, text):
        comment = Comment(text)
        post.add_comment(comment)
        return comment

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username and self.email == other.email
        return False


class Game:
    """Game."""
    def __init__(self, title, release_date, description, developer, processor, graphics_card, operating_system):
        self.title = title
        self.release_date = release_date
        self.description = description
        self.developer = developer
        self.processor = processor
        self.graphics_card = graphics_card
        self.operating_system = operating_system

    def __eq__(self, other):
        if isinstance(other, Game):
            return (
                self.title == other.title and
                self.release_date == other.release_date and
                self.description == other.description and
                self.developer == other.developer and
                self.processor == other.processor and
                self.graphics_card == other.graphics_card and
                self.operating_system == other.operating_system
            )
        return False


@dataclass(frozen=True)
class Developer:
    """Developer."""
    name: str


@dataclass(frozen=True)
class GraphicsCard:
    """Graphics Card."""
    name: str
    rating: float


@dataclass(frozen=True)
class Processor:
    """Processor."""
    name: str
    rating: float


@dataclass(frozen=True)
class OperatingSystem:
    """Operating System."""
    name: str
    rating: float


class Post:
    """Post."""
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.comments = []

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.title == other.title and \
                   self.description == other.content
        return False

    def add_comment(self, comment):
        self.comments.append(comment)


class Comment:
    """Post Comment."""
    def __init__(self, text, user):
        self.text = text
        self.user = user
        self.creation_date = datetime.datetime.now()

    def __eq__(self, other):
        if isinstance(other, Comment):
            return self.text == other.text
        return False


class Collection:
    """Collection."""
    def __init__(self, name):
        self.name = name
        self.games = []

    def __eq__(self, other):
        if isinstance(other, Collection):
            return (
                self.name == other.name and
                self.games == other.games
            )
        return False


class GameSearch:
    def __init__(self):
        self.graphic_model = GraphicsCard
        self.os_model = OperatingSystem
        self.processor_model = Processor

    def __eq__(self, other):
        if isinstance(other, GameSearch):
            return (
                    self.graphic_model == other.graphic_model and
                    self.os_model == other.os_model and
                    self.processor_model == other.processor_model
            )
        return False


class PostService:
    @staticmethod
    def add_comment_to_post(post, text, user):
        comment = Comment(text, user)
        post.add_comment(comment)

    @staticmethod
    def get_comments_for_post(post):
        return post.comments

    @staticmethod
    def get_comments_by_user(post, user):
        return [comment for comment in post.comments if comment.user == user]

    @staticmethod
    def get_comments_since_date(post, date):
        return [comment for comment in post.comments if
                comment.creation_date >= date]


class CollectionService:
    @staticmethod
    def create_collection(name):
        return Collection(name)

    @staticmethod
    def add_game_to_collection(collection, game):
        collection.games.append(game)

    @staticmethod
    def remove_game_from_collection(collection, game):
        if game in collection.games:
            collection.games.remove(game)


class GameSearchService:
    def __init__(self, games):
        self.games = games

    def search_games(self, graphic_model=None, os_model=None,
                     processor_model=None, developer_name=None):
        filtered_games = self.games

        if graphic_model:
            filtered_games = [game for game in filtered_games if
                              game.graphics_card == graphic_model]
        if os_model:
            filtered_games = [game for game in filtered_games if
                              game.operating_system == os_model]
        if processor_model:
            filtered_games = [game for game in filtered_games if
                              game.processor == processor_model]
        if developer_name:
            filtered_games = [game for game in filtered_games if
                              game.developer.name == developer_name]

        return filtered_games


class FriendshipService:
    @staticmethod
    def add_friend(user, friend):
        if friend not in user.friends:
            user.friends.append(friend)

    @staticmethod
    def remove_friend(user, friend):
        if friend in user.friends:
            user.friends.remove(friend)
