from tools.models import ToolCredential


def tools_without_credentials(owner, tools):
    tools_pending_credentials = []
    for tool in tools:
        has_credential = ToolCredential.objects.filter(owner=owner, tool=tool).exists()
        if not has_credential:
            tools_pending_credentials.append(tool)

    return tools_pending_credentials
