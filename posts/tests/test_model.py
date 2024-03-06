import pytest

from posts.conftest import post_factory


@pytest.mark.django_db
def test_post_model(post_factory):
    post = post_factory(text="test text")
    assert post.text == "test text"


@pytest.mark.django_db
def test_post_str_representation(post_factory):
    post = post_factory(text="test text")
    assert str(post) == post.text
