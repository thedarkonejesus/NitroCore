"""
GUI Module - Thread-safe, modern flat-styled UI components for NitroCore.
Exposes optimized widget canvas systems and layout frameworks cleanly.
"""

__version__ = "1.0.0"
__author__ = "NitroCore Team"

# 1. Import your fully optimized, modern flat-styled components cleanly
from .window import Window
from .button import CustomButton
from .entry import CustomEntry
from .frame import CustomFrame

# NOTE: Making sure fallback guards or placeholders are accounted for 
# if Label or LayoutManager files are being carried over or polished.
try:
    from .label import Label
except ImportError:
    import tkinter as tk
    class Label(tk.Label): pass

try:
    from .layout import LayoutManager
except ImportError:
    class LayoutManager: pass


# 2. Explicitly export the synchronized, high-performance UI components
__all__ = [
    "Window",
    "CustomButton",
    "Label",
    "CustomEntry",
    "CustomFrame",
    "LayoutManager"
]
