from repositories import *
from models import *

# Создание экземпляров разработчиков
developer_1 = Developer("Developer 1")
developer_2 = Developer("Developer 2")

# Создание экземпляров процессоров и видеокарт
processor_1 = Processor("Processor 1", 4.5)
processor_2 = Processor("Processor 2", 5.0)
graphics_card_1 = GraphicsCard("Graphics Card 1", 4.8)
graphics_card_2 = GraphicsCard("Graphics Card 2", 4.9)

# Создание экземпляров операционных систем
os_1 = OperatingSystem("Windows 11", 4.5)
os_2 = OperatingSystem("Windows 10", 4.7)

# Создание экземпляров игр
game_1 = Game("Game 1", "2023-01-01", "Description 1", developer_1, processor_1, graphics_card_1, os_1)
game_2 = Game("Game 2", "2023-02-01", "Description 2", developer_2, processor_2, graphics_card_2, os_2)

# Создание экземпляров пользователей
user_1 = User("user1", "user1@example.com", "password1")
user_2 = User("user2", "user2@example.com", "password2")

# Создание экземпляров постов и комментариев
post_1 = user_1.write_post("Post Title 1", "Post Description 1")
comment_1 = user_2.write_comment(post_1, "Comment Text 1")

# Создание экземпляров коллекций
collection_1 = Collection()
collection_1.add_game(game_1)
collection_1.add_game(game_2)

# Создание экземпляров для GameSearch
game_search_repo = GameSearchRepository([game_1, game_2])


# Создание экземпляров фейковых репозиториев
developer_repo = DeveloperRepository()
developer_repo.add_developer(developer_1)
developer_repo.add_developer(developer_2)

processor_repo = ProcessorRepository()
processor_repo.add_processor(processor_1)
processor_repo.add_processor(processor_2)

graphics_card_repo = GraphicsCardRepository()
graphics_card_repo.add_graphics_card(graphics_card_1)
graphics_card_repo.add_graphics_card(graphics_card_2)

os_repo = OperatingSystemRepository()
os_repo.add_operating_system(os_1)
os_repo.add_operating_system(os_2)

game_repo = GameRepository()
game_repo.add_game(game_1)
game_repo.add_game(game_2)

user_repo = UserRepository()
user_repo.add_user(user_1)
user_repo.add_user(user_2)
all_users = user_repo.get_all_users()

post_repo = PostRepository()
post_repo.add_post(post_1)

comment_repo = CommentRepository()
comment_repo.add_comment(comment_1)

collection_repo = CollectionRepository()
collection_repo.add_collection(collection_1)

