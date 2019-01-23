import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer

from factories.tools.tool_factory import ToolFactory
from tools.views import tools_without_credentials


@pytest.fixture
def owner(db):
    return mixer.blend(User)


@pytest.fixture
def tools_with_credentials(owner):
    tools = []
    for tool in ToolFactory.build_batch(10):
        instance = mixer.blend('tools.Tool', name=tool.name)
        mixer.blend('tools.ToolCredential', owner=owner, tool=instance)
        tools.append(instance)
    return tools


@pytest.fixture
def tools_with_no_credentials(db):
    tools = []
    for tool in ToolFactory.build_batch(10):
        tools.append(tool)
        mixer.blend('tools.Tool', name=tool.name)
    return tools


def test_project_owner_has_tool_credentials(owner, tools_with_credentials):
    assert len(tools_without_credentials(owner, tools_with_credentials)) == 0


def test_project_owner_has_no_tool_credentials(owner, tools_with_no_credentials):
    assert len(tools_without_credentials(owner, tools_with_no_credentials)) == 10

