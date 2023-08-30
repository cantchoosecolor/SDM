
class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user_by_username(self, username):
        return next((user for user in self.users if user.username == username),
                    None)

    def get_user_by_email(self, email):
        return next((user for user in self.users if user.email == email), None)

    def get_all_users(self):
        for user in self.users:
            print(f"Username: {user.username}, Email: {user.email}")
        return self.users

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


class CollectionRepository:
    def __init__(self):
        self.collections = []

    def add_collection(self, collection):
        self.collections.append(collection)

    def get_collection_by_user(self, user):
        return [collection for collection in self.collections if
                collection.user == user]

    def get_collection_by_id(self, collection_id):
        return next((collection for collection in self.collections if
                     collection.id == collection_id), None)


class PostRepository:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_posts_by_user(self, user):
        return [post for post in self.posts if post.user == user]

    def get_post_by_id(self, post_id):
        return next((post for post in self.posts if post.id == post_id), None)

    def delete_post(self, post):
        self.posts.remove(post)

    def get_all_posts(self):
        return self.posts


class CommentRepository:
    def __init__(self):
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments_by_post(self, post):
        return [comment for comment in self.comments if comment.post == post]

    def get_comment_by_id(self, comment_id):
        return next(
            (comment for comment in self.comments if comment.id == comment_id),
            None)

    def delete_comment(self, comment):
        self.comments.remove(comment)

    def get_all_comments(self):
        return self.comments


class GameRepository:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def get_game_by_title(self, title):
        return next((game for game in self.games if game.title == title), None)

    def search_games_by_developer(self, developer_name):
        return [game for game in self.games if
                game.developer.name == developer_name]

    def search_games_by_processor(self, processor_name, min_rating=None):
        if min_rating is None:
            return [game for game in self.games if
                    game.processor.name == processor_name]
        else:
            return [game for game in self.games if
                    game.processor.name == processor_name and game.processor.rating >= min_rating]

    def delete_game(self, game):
        self.games.remove(game)

    def get_all_games(self):
        return self.games


class DeveloperRepository:
    def __init__(self):
        self.developers = []

    def add_developer(self, developer):
        self.developers.append(developer)

    def get_developer_by_name(self, name):
        return next((developer for developer in self.developers if
                     developer.name == name), None)

    def delete_developer(self, developer):
        self.developers.remove(developer)

    def get_all_developers(self):
        return self.developers


class GraphicsCardRepository:
    def __init__(self):
        self.graphics_cards = []

    def add_graphics_card(self, graphics_card):
        self.graphics_cards.append(graphics_card)

    def get_graphics_card_by_name(self, name):
        return next((graphics_card for graphics_card in self.graphics_cards if
                     graphics_card.name == name), None)

    def delete_graphics_card(self, graphics_card):
        self.graphics_cards.remove(graphics_card)

    def get_all_graphics_cards(self):
        return self.graphics_cards


class ProcessorRepository:
    def __init__(self):
        self.processors = []

    def add_processor(self, processor):
        self.processors.append(processor)

    def get_processor_by_name(self, name):
        return next((processor for processor in self.processors if
                     processor.name == name), None)

    def delete_processor(self, processor):
        self.processors.remove(processor)

    def get_all_processors(self):
        return self.processors


class OperatingSystemRepository:
    def __init__(self):
        self.operating_systems = []

    def add_operating_system(self, operating_system):
        self.operating_systems.append(operating_system)

    def get_operating_system_by_name(self, name):
        return next(
            (operating_system for operating_system in self.operating_systems if
             operating_system.name == name), None)

    def delete_operating_system(self, operating_system):
        self.operating_systems.remove(operating_system)

    def get_all_operating_systems(self):
        for os in self.operating_systems:
            print(f"Operating System: {os.name}, Rating: {os.rating}")
        return self.operating_systems


class GameSearchRepository:
    def __init__(self, games):
        self.games = games

    def search_by_developer(self, developer_name):
        return [game for game in self.games if
                game.developer.name == developer_name]

    def search_by_processor(self, processor_name, min_rating=None):
        if min_rating is None:
            return [game for game in self.games if
                    game.processor.name == processor_name]
        else:
            return [game for game in self.games if
                    game.processor.name == processor_name and
                    game.processor.rating >= min_rating]

    def search_by_graphics_card(self, graphics_card_name, min_rating=None):
        if min_rating is None:
            return [game for game in self.games if
                    game.graphics_card.name == graphics_card_name]
        else:
            return [game for game in self.games if
                    game.graphics_card.name == graphics_card_name and
                    game.graphics_card.rating >= min_rating]

    def search_by_operating_system(self, os_name, min_rating=None):
        if min_rating is None:
            return [game for game in self.games if
                    game.operating_system.name == os_name]
        else:
            return [game for game in self.games if
                    game.operating_system.name == os_name and
                    game.operating_system.rating >= min_rating]





