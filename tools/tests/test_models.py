import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModels:

    def test_tool_is_created(self):
        tool_credential = mixer.blend('tools.ToolCredential', token="123456")
        assert tool_credential.is_created == True

    def test_tool_is_not_created(self):
        tool_credential = mixer.blend('tools.ToolCredential', token="")
        assert tool_credential.is_created == False
