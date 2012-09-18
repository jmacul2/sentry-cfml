sentry-cfml
==========

sentry-cfml is an plugin `Sentry <https://www.getsentry.com/welcome/>`_ that provides
a custom interface that is used with `raven-cfml <https://github.com/jmacul2/raven-cfml>`_.

Installation
------------

Install source from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~

To install the source code:

::

    $ git clone git://github.com/jmacul2/sentry-cfml.git



Configuration
~~~~~~~~~~~~~

1. Add sentry-cfml to the installed django apps:

::

   INSTALLED_APPS = (
      ...
      'sentry_cfml'
      ...
   )

2. Reference the interface in the init of the raven-cfml client:

::

   <cfset ravenConfig = structNew()>
   ...
   <cfset ravenConfig.customHttpInterface = 'sentry_cfml.interfaces.CFMLHttp'>
   ...
   <cfset ravenClient = createObject('component', '[path.to.raven].lib.client').init(argumentCollection=ravenConfig)>

Resources
---------

* `Bug Tracker <http://github.com/jmacul2/sentry-cfml/issues>`_
* `Code <http://github.com/jmacul2/sentry-cfml>`_