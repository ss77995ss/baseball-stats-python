"""Logging setup for the package.

The package only logs; it never configures the root logger. Applications
decide what to show, e.g. logging.basicConfig(level=logging.INFO).
"""

import logging

PACKAGE_LOGGER_NAME = 'baseball_stats_python'

package_logger = logging.getLogger(PACKAGE_LOGGER_NAME)
package_logger.addHandler(logging.NullHandler())


def enable_debug_logging() -> None:
    """Print this package's DEBUG logs to stderr (used by debug=True)."""
    if not any(getattr(h, '_bsp_debug', False) for h in package_logger.handlers):
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(name)s %(levelname)s: %(message)s'))
        handler._bsp_debug = True
        package_logger.addHandler(handler)
    package_logger.setLevel(logging.DEBUG)
