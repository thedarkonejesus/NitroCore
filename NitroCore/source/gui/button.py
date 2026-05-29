"""
Custom Button component featuring hover feedback loops and flat theme integrations.
Optimized to deliver smooth UI interactions matching modern system aesthetics.
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Union, Tuple


class CustomButton:
    """
    High-performance flat-styled button component with native hover transitions 
    and unified styling defaults built for NitroCore.
    """
    
    def __init__(
        self,
        parent: tk.Widget,
        text: str,
        command: Optional[Callable] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        bg_color: str = "#2A2D32",       # Sleek charcoal/slate default
        fg_color: str = "#FFFFFF",       # High-contrast white text
        hover_color: str = "#40444B",    # Lightened highlight state
        font: Tuple[str, int, str] = ("Segoe UI", 10, "normal")
    ):
        """Initialize customized widget properties with responsive state trackers."""
        self.parent = parent
        self.text = text
        self.command = command
        
        # Color profile configurations
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.hover_color = hover_color
        self.is_enabled = True

        # Initialize underlying element using flat styling parameters
        self.widget = tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            height=height,
            bg=self.bg_color,
            fg=self.fg_color,
            font=font,
            activebackground=self.hover_color,
            activeforeground=self.fg_color,
            relief="flat",               # Removes the dated 90s border layout
            bd=0,                        # Zeroes out legacy borders
            cursor="hand2"               # Changes cursor to interactive pointer
        )
        
        # Bind micro-interaction event routines for seamless UX response
        self.widget.bind("<Enter>", self._on_mouse_enter)
        self.widget.bind("<Leave>", self._on_mouse_leave)

    def pack(self, **kwargs) -> None:
        """Expose layout pack control."""
        self.widget.pack(**kwargs)

    def grid(self, row: int, column: int, **kwargs) -> None:
        """Expose layout grid structure control."""
        self.widget.grid(row=row, column=column, **kwargs)

    def place(self, **kwargs) -> None:
        """Expose precise pixel positioning control."""
        self.widget.place(**kwargs)

    def set_command(self, command: Callable) -> None:
        """Update click routine target dynamically."""
        self.command = command
        self.widget.config(command=command)

    def enable(self) -> None:
        """Re-activate interaction pathways and reset default background shades."""
        self.is_enabled = True
        self.widget.config(state="normal", bg=self.bg_color, cursor="hand2")

    def disable(self) -> None:
        """Freeze interactions and apply modern muted gray indicators."""
        self.is_enabled = False
        self.widget.config(state="disabled", bg="#1E1F22", fg="#5865F2", cursor="arrow")

    def set_text(self, text: str) -> None:
        """Update label value string data smoothly."""
        self.text = text
        self.widget.config(text=text)

    def _on_mouse_enter(
