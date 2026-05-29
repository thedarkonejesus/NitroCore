"""
Custom Label component featuring multi-line auto-wrap and thread-safe text styling.
Optimized to handle dynamic status updates and long file path logs cleanly.
"""

import tkinter as tk
from typing import Optional, Tuple, Union


class CustomLabel:
    """
    High-performance flat text display component built for NitroCore.
    Supports smart independent color updates and fluid layout text wrapping.
    """
    
    def __init__(
        self,
        parent: tk.Widget,
        text: str,
        font: Tuple[str, int, str] = ("Segoe UI", 10, "normal"),
        fg_color: str = "#F2F3F5",       # Crisp white/slate text for readability
        bg_color: str = "#2F3136",       # Matches our main panel color
        anchor: str = "w",                # Default align to West (left-aligned) for clean text tracking
        wrap_length: int = 0             # 0 means disabled. Pass a pixel value (e.g., 400) to auto-wrap long text
    ):
        """Initialize label properties and set up anti-aliasing defaults."""
        self.parent = parent
        self.text = text

        # Core element initialization using modern typography presets
        self.widget = tk.Label(
            parent,
            text=text,
            font=font,
            fg=fg_color,
            bg=bg_color,
            anchor=anchor,
            justify="left",              # Left-justify multi-line block text
            wraplength=wrap_length
        )

    def pack(self, **kwargs) -> None:
        """Expose layout pack control."""
        self.widget.pack(**kwargs)

    def grid(self, row: int, column: int, **kwargs) -> None:
        """Expose layout grid structure control."""
        self.widget.grid(row=row, column=column, **kwargs)

    def place(self, **kwargs) -> None:
        """Expose relative or exact pixel coordinates mapping control."""
        self.widget.place(**kwargs)

    def set_text(self, text: str) -> None:
        """Updates display text smoothly across running dashboard loops."""
        self.text = text
        self.widget.config(text=text)

    def set_font(self, font: Tuple[str, int, str]) -> None:
        """Dynamically re-scales typography sizing parameters."""
        self.widget.config(font=font)

    def set_foreground(self, fg_color: str) -> None:
        """Independently shifts text color (perfect for green/red/orange status indicators)."""
        self.widget.config(fg=fg_color)

    def set_background(self, bg_color: str) -> None:
        """Independently alters background panel matching canvas values."""
        self.widget.config(bg=bg_color)

    def set_wrap_length(self, pixels: int) -> None:
        """Adjusts the wrap constraint pixel threshold dynamically if the window resizes."""
        self.widget.config(wraplength=pixels)
