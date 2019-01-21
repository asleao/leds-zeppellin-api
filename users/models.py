from django.contrib.auth.models import User

from tools.models import ToolCredential


def have_tool_credential(self, tool):
    tool_credential = ToolCredential.objects.filter(owner=self, tool=tool)
    return tool_credential.count() > 0


User.add_to_class('have_tool_credential', have_tool_credential)
