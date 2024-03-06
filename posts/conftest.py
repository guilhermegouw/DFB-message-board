import pytest
from posts.factories import PostFactory

@pytest.fixture
def post_factory():
    return PostFactory
