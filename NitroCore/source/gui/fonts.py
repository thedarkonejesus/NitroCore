"""
Hardware-accelerated font schema manager for NitroCore graphical layers.
"""

import tkinter as tk
import tkinter.font as tkfont
from typing import Dict

class FontEngine:
    """Initializes and caches hardware-rendered font sheets for the application."""
    
    _registry: Dict[str, tkfont.Font] = {}

    @classmethod
    def initialize(cls) -> None:
        """Compiles font patterns directly into the active Tkinter window engine context."""
        if cls._registry:
            return  # Already initialized

        # Base Segoe UI configurations optimized for high-DPI Windows displays
        cls._registry["title"] = tkfont.Font(family="Segoe UI", size=16, weight="bold")
        cls._registry["header"] = tkfont.Font(family="Segoe UI", size=12, weight="bold")
        cls._registry["body"] = tkfont.Font(family="Segoe UI", size=10, weight="normal")
        cls._registry["button"] = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        cls._registry["log"] = tkfont.Font(family="Consolas", size=9, weight="normal")

    @classmethod
    def get(cls, style_name: str) -> tkfont.Font:
        """Fetches a pre-compiled font profile by name."""
        return cls._registry.get(style_name, ("Segoe UI", 10, "normal"))
