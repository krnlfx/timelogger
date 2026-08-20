"""TimeLogger: Logs time spent on activities and prints weekly breakdowns."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]