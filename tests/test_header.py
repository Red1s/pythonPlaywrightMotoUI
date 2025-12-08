import pytest
from playwright.sync_api import Page
from pages.header import Header


@pytest.mark.smoke
def test_avatar_visible(logged_in_user):
    logged_in_user.ensure_avatar_circle_is_visible()

