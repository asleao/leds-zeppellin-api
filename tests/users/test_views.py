import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer

from users.views import has_tool_credential


@pytest.fixture
def user(db):
    return mixer.blend(User)


@pytest.fixture
def tool(db):
    return mixer.blend("tools.Tool")


def test_user_has_tool_credential(user, tool):
    mixer.blend("tools.ToolCredential", owner=user, tool=tool)

    assert has_tool_credential(user=user, tool=tool) == True


def test_user_not_has_tool_credential(user, tool):
    assert has_tool_credential(user=user, tool=tool) == False
