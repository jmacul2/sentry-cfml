sentry-cfml
==========

sentry-cfml is a `Sentry <https://www.getsentry.com/welcome/>`_ plugin that provides
a custom interface that is used with `raven-cfml <https://github.com/jmacul2/raven-cfml>`_.

Installation
------------

Install source from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~

To install the source code:

::

    $ pip install -e git+https://github.com/jmacul2/sentry-cfml.git#egg=sentry_cfml-dev



Configuration
~~~~~~~~~~~~~

Reference the interface in the init of the raven-cfml client:

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
