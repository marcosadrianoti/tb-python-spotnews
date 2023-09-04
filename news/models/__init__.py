from django.db import models  # noqa F401

try:
    from news.models.category_model import Categories  # noqa F401
    from news.models.user_model import Users  # noqa F401
    from news.models.news_model import News  # noqa F401
except ModuleNotFoundError:
    pass
