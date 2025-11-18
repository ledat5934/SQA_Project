* Added the new ``swallowed-exception`` and ``empty-except-body`` warnings to
  highlight exception handlers that do not perform any meaningful action and
  therefore hide bugs.

* Added the new ``resource-leak-maybe`` refactoring message that emits a
  dedicated suggestion when a resource is neither managed by a ``with`` block
  nor explicitly closed.

