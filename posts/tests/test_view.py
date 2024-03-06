import pytest

from django.urls import reverse

from posts.conftest import post_factory


def test_home_page_status_code(client, db):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


def test_home_page_template(client, db):
    url = reverse("home")
    response = client.get(url)
    assert "home.html" in (t.name for t in response.templates)


def test_home_page_contains_right_html(client, db):
    url = reverse("home")
    response = client.get(url)
    assert b"<h1>Message board homepage</h1>" in response.content


@pytest.mark.django_db
def test_home_page_contains_posts(client, db, post_factory):
    post = post_factory(text="test text")
    url = reverse("home")
    response = client.get(url)
    assert "test text" in response.content.decode()
