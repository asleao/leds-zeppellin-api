from users.views import has_tool_credential


def tools_without_credentials(owner, tools):
    tools_pending_credentials = []
    for tool in tools:
        if not has_tool_credential(owner, tool):
            tools_pending_credentials.append(tool)

    return tools_pending_credentials
