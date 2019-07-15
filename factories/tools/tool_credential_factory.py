import factory

from tools.models import ToolCredential


class ToolCredentialFactory(factory.Factory):
    class Meta:
        model = ToolCredential
