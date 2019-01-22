import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer


@pytest.fixture
def user(db):
    return mixer.blend(User)


@pytest.fixture
def tool(db):
    return mixer.blend("tools.Tool")


def test_user_has_tool_credential(user, tool):
    mixer.blend("tools.ToolCredential", owner=user, tool=tool)

    assert user.has_tool_credential(tool=tool) == True


def test_user_not_has_tool_credential(user, tool):
    assert user.has_tool_credential(tool=tool) == False
