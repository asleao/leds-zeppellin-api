from django.contrib.auth.models import User
from django.test import TestCase
from mixer.backend.django import mixer


class TestModels(TestCase):

    def setUp(self):
        self.user = mixer.blend(User)
        self.tool = mixer.blend("tools.Tool")

    def test_user_has_tool_credential(self):
        mixer.blend("tools.ToolCredential", owner=self.user, tool=self.tool)

        assert self.user.has_tool_credential(tool=self.tool) == True

    def test_user_not_has_tool_credential(self):
        assert self.user.has_tool_credential(tool=self.tool) == False
