from projects.models import ToolMessage, CollaboratorMessage
from tools.models import ToolCredential


def collaborator_messages(signal_data):
    messages = []
    for collaborator in signal_data.collaborators:
        for tool in signal_data.instance.tools.all():
            credential = ToolCredential.objects.get(owner=signal_data.instance.owner, tool=tool)
            message = CollaboratorMessage(signal_data.instance.language.name, signal_data.instance.name,
                                          signal_data.action, tool.name, collaborator.username, credential.token)
            messages.append(message)
    return messages


def tool_messages(signal_data):
    messages = []
    for tool in signal_data.tools:
        message = ToolMessage(signal_data.instance.language.name, signal_data.instance.name, signal_data.action,
                              tool.name)
        messages.append(message)
    return messages


def send_messages(queue_sufix, messages):
    for message in messages:
        message.message(queue_sufix).send_message()
