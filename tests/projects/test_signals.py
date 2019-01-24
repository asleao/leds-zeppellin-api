import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer

from factories.projects.tool_signal_data_factory import ToolSignalDataFactory
from factories.tools.tool_factory import ToolFactory


@pytest.fixture
def owner(db):
    return mixer.blend(User)


@pytest.fixture()
def project(owner):
    return mixer.blend('projects.Project', owner=owner)


@pytest.fixture
def tools_with_credentials(owner):
    tools = {}
    for tool in ToolFactory.build_batch(10):
        instance = mixer.blend('tools.Tool', name=tool.name)
        mixer.blend('tools.ToolCredential', owner=owner, tool=instance)
        tools[instance.id] = instance
    return tools


@pytest.fixture
def signal_data(db):
    return ToolSignalDataFactory()


# def test_send_project_to_queue(signal_data):
    # tool_messages(signal_data)
    # assert len(tool_messages) == 10
