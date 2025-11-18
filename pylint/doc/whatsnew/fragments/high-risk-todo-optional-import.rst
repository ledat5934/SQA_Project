* Added the ``high-risk-todo`` message (``W0512``) which can be enabled by providing
  a ``high-risk-fixme-rgx`` pattern to flag critical TODO/FIXME notes separately from
  regular ``fixme`` warnings.
* Added the ``optional-import-error`` message (``W0405``) alongside the new
  ``optional-import-modules`` option so optional dependencies can be linted as
  warnings instead of hard errors when they are not available.

