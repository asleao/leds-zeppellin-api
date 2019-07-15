import pytest

from mixer.backend.django import mixer


@pytest.fixture
def credential(request, db):
    return mixer.blend('tools.ToolCredential', token=request.param)


@pytest.mark.parametrize('credential', ['123456'], indirect=True)
def test_tool_is_created(credential):
    assert credential.is_created == True


@pytest.mark.parametrize('credential', [''], indirect=True)
def test_tool_is_not_created(credential):
    assert credential.is_created == False
