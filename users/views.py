from tools.models import ToolCredential


def has_tool_credential(user, tool):
    return ToolCredential.objects.filter(owner=user, tool=tool).exists()
