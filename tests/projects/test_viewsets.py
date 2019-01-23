import pytest
from django.test import RequestFactory

from factories.projects.project_factory import ProjectFactory


@pytest.fixture(scope='module')
def factory():
    return RequestFactory()


def test_project_tools_success():
    project = ProjectFactory()
    # TODO: Continuar o test.
    assert project.name != ""
