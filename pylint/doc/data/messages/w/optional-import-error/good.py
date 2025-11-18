"""Example with guarded optional dependency."""

try:
    import optional_dependency
except ImportError:  # Optional, handled gracefully.
    optional_dependency = None

