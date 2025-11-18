"""Test optional dependency imports."""
# pylint: disable=missing-module-docstring, unused-import

import totally_missing  # [optional-import-error]
import another_missing  # [import-error]

