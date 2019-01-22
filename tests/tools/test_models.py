from django.test import TestCase

from mixer.backend.django import mixer


class TestModels(TestCase):

    def test_tool_is_created(self):
        tool_credential = mixer.blend('tools.ToolCredential', token="123456")
        assert tool_credential.is_created == True

    def test_tool_is_not_created(self):
        tool_credential = mixer.blend('tools.ToolCredential', token="")
        assert tool_credential.is_created == False
