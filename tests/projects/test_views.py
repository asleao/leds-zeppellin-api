import factory
import pytest
from django.contrib.auth.models import User
from django.db.models import signals
from mixer.backend.django import mixer

from factories.projects.collaborator_signal_data_factory import CollaboratorSignalDataFactory
from factories.projects.tool_signal_data_factory import ToolSignalDataFactory
from factories.tools.tool_factory import ToolFactory
from projects.views import tool_messages, collaborator_messages


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
@factory.django.mute_signals(signals.pre_save, signals.post_save, signals.m2m_changed)
def tool_signal_data(project, tools_with_credentials):
    return ToolSignalDataFactory(instance=project, action='post', tools=tools_with_credentials.values())


@pytest.fixture
def collaborators(db):
    return mixer.cycle(1).blend(User)


@pytest.fixture
@factory.django.mute_signals(signals.pre_save, signals.post_save, signals.m2m_changed)
def collaborator_signal_data(project, collaborators, tools_with_credentials):
    project.tools.set(tools_with_credentials.keys())
    return CollaboratorSignalDataFactory(instance=project, action='post',
                                         collaborators=collaborators)


def test_tool_messages(tool_signal_data):
    messages = tool_messages(tool_signal_data)
    assert len(messages) == 10

# TODO fix test
# def test_collaborator_messages(collaborator_signal_data):
#     messages = collaborator_messages(collaborator_signal_data)
#     assert len(messages) == 10
