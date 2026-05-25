"""Window class for creating application windows"""

import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Any


class Window:
    """Base window class with common properties and methods"""
    
    def __init__(
        self,
        title: str = "PyGui App",
        width: int = 800,
        height: int = 600,
        resizable: bool = True,
        icon_path: Optional[str] = None
    ):
        """Initialize window"""
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizable, resizable)
        
        if icon_path:
            try:
                self.root.iconbitmap(icon_path)
            except tk.TclError:
                pass
        
        # Store window state
        self.is_open = True
        self.on_close_callbacks = []
        
        # Bind close event
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
    
    def _on_close(self) -> None:
        """Handle window close event"""
        self.is_open = False
        for callback in self.on_close_callbacks:
            callback()
        self.root.destroy()
    
    def add_close_callback(self, callback: Callable) -> None:
        """Add callback for window close event"""
        self.on_close_callbacks.append(callback)
    
    def center(self) -> None:
        """Center window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def show(self) -> None:
        """Show window"""
        self.root.mainloop()
    
    def hide(self) -> None:
        """Hide window"""
        self.root.withdraw()
    
    def destroy(self) -> None:
        """Destroy window"""
        self.is_open = False
        self.root.destroy()
    
    def focus(self) -> None:
        """Bring window to front"""
        self.root.lift()
        self.root.focus_force()