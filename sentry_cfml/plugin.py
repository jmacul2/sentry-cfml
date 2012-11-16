import sentry_cfml
from sentry.plugins import Plugin


class CFMLPlugin(Plugin):
    title = 'Sentry CFML'
    slug = 'sentry-cfml'
    description = 'A plugin for CFML that adds a custom interface specific to request variables used in CFML'
    version = sentry_pluginname.VERSION

    author = 'Jay McEntire'
    author_url = 'https://github.com/jmacul2/sentry-cfml'

    def widget(self, request, group, **kwargs):
        pass
