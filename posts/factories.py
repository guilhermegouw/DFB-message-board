import factory

from .models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    text = factory.Faker("sentence", nb_words=10)
