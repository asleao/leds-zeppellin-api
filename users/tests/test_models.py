import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModels:

    def test_user_have_tool_credential(self):
        user = mixer.blend(User)
        tool = mixer.blend("tools.Tool")
        mixer.blend("tools.ToolCredential", owner=user, tool=tool)

        assert user.have_tool_credential(tool=tool) == True

    def test_user_not_have_tool_credential(self):
        user = mixer.blend(User)
        tool = mixer.blend("tools.Tool")

        assert user.have_tool_credential(tool=tool) == False
