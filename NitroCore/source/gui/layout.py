"""Layout manager for organizing widgets"""

import tkinter as tk
from typing import List, Tuple, Dict, Any, Optional


class LayoutManager:
    """Layout manager for organizing widgets in different layouts"""
    
    @staticmethod
    def vertical_stack(widgets: List[tk.Widget], spacing: int = 5) -> None:
        """Stack widgets vertically with spacing"""
        for widget in widgets:
            widget.pack(fill=tk.X, padx=10, pady=spacing)
    
    @staticmethod
    def horizontal_stack(widgets: List[tk.Widget], spacing: int = 5) -> None:
        """Stack widgets horizontally with spacing"""
        for widget in widgets:
            widget.pack(side=tk.LEFT, padx=spacing)
    
    @staticmethod
    def grid_layout(
        widgets: List[tk.Widget],
        rows: int,
        cols: int,
        spacing: Tuple[int, int] = (5, 5),
        sticky: str = 'ew'
    ) -> None:
        """Arrange widgets in a grid"""
        for i, widget in enumerate(widgets):
            row = i // cols
            col = i % cols
            widget.grid(
                row=row,
                column=col,
                padx=spacing[0],
                pady=spacing[1],
                sticky=sticky
            )
    
    @staticmethod
    def form_layout(widgets: List[Tuple[str, tk.Widget]], spacing: int = 10) -> None:
        """Create form layout with labels and controls"""
        for i, (label_text, control) in enumerate(widgets):
            label = tk.Label(control.master, text=label_text)
            label.grid(row=i, column=0, sticky='w', padx=spacing, pady=spacing//2)
            control.grid(row=i, column=1, sticky='ew', padx=spacing, pady=spacing//2)
    
    @staticmethod
    def responsive_grid(
        widgets: List[tk.Widget],
        min_width: int = 300,
        max_columns: int = 4
    ) -> None:
        """Create responsive grid layout"""
        parent = widgets[0].master
        parent.columnconfigure(0, weight=1)
        
        row = 0
        col = 0
        
        for widget in widgets:
            widget.grid(
                row=row,
                column=col,
                sticky='ew',
                padx=5,
                pady=5
            )
            
            col += 1
            if col >= max_columns:
                col = 0
                row += 1
                
            parent.rowconfigure(row, weight=1)