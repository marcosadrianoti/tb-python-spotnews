try:
    from news.models.category_model import Categories
except ModuleNotFoundError:
    Categories = None

try:
    from news.models.user_model import Users
except ModuleNotFoundError:
    Users = None

try:
    from news.models.news_model import News
except ModuleNotFoundError:
    News = None
from news.scripts.data import authors, categories, news


def create_users(user_model):
    for author in authors:
        user_model.objects.create(
            name=author["name"],
            email=author["email"],
            password=author["password"],
            role=author["role"],
        )


def create_categories(categories_model):
    for category in categories:
        categories_model.objects.create(name=category["name"])


def create_news(news_model, categories_model, user_model):
    for new in news:
        n = news_model.objects.create(
            title=new["title"],
            content=new["content"],
            author=user_model.objects.get(name=new["author"]),
            created_at=new["created_at"],
            image=new["image"],
        )
        category = categories_model.objects.get(name=new["category"])
        n.categories.add(category)


def run():
    if Categories is not None and not Categories.objects.all():
        create_categories(Categories)
        print("Categories created successfully!")

    if Users is not None and not Users.objects.all():
        create_users(Users)
        print("Users created successfully!")

    if (
        (Users is not None and Users.objects.all())
        and (Categories is not None and Categories.objects.all())
        and (News is not None and not News.objects.all())
    ):
        create_news(News, Categories, Users)
        print("News created successfully!")
