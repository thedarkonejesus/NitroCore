"""PyGui - Python GUI framework for cross-platform applications"""

__version__ = "1.0.0"
__author__ = "DeepHat Team"

# Import core classes
from .window import Window
from .button import Button
from .label import Label
from .entry import Entry
from .frame import Frame
from .layout import LayoutManager

__all__ = [
    "Window",
    "Button",
    "Label",
    "Entry",
    "Frame",
    "LayoutManager"
]