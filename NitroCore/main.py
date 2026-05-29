"""
NitroCore Windows System Optimizer - Primary Application Entry Point.
Initializes critical OS mutex bounds, anti-aliasing engines, and the GUI loop.
"""

import sys
from src.utils.lifecycle import LifecycleManager
from src.gui.window import Window
from src.gui.fonts import FontEngine
from src.gui.frame import CustomFrame
from src.gui.button import CustomButton
from src.gui.label import CustomLabel

def app_emergency_shutdown():
    """Triggered automatically if the process is terminated abruptly."""
    print("[Shutdown] Releasing open system hooks, logs, and handles safely.")
    # Perform your dynamic in-memory pointer cleanups here

def run_optimization_pipeline():
    """Placeholder trigger showing how background workers are invoked."""
    print("[Engine] Dispatched asynchronous system optimization tasks...")

def bootstrap():
    """Validates runtime conditions, boots the graphics canvas, and displays the UI."""
    # 1. Enforce single-instance mutex limits before spinning up memory vectors
    LifecycleManager.enforce_single_instance()
    
    # 2. Bind emergency exiting routines
    LifecycleManager.register_emergency_cleanup(app_emergency_shutdown)
    
    # 3. Spawn primary dark-themed workspace window manager
    app_window = Window(
        title="NitroCore Windows Optimizer v1.0.0",
        width=950,
        height=650,
        resizable=False
    )
    
    # 4. Spin up the font engine instantly inside the active Tkinter canvas context
    FontEngine.initialize()
    
    # 5. Assemble your dashboard panels cleanly using your custom UI classes
    main_panel = CustomFrame(app_window.canvas)
    main_panel.pack(fill="both", expand=True, padx=20, pady=20)
    
    title_lbl = CustomLabel(
        parent=main_panel.canvas,
        text="System Optimization Dashboard",
        font=FontEngine.get("title")
    )
    title_lbl.pack(anchor="w", pady=(0, 20))
    
    optimize_btn = CustomButton(
        parent=main_panel.canvas,
        text="RUN NITRO CORE OPTIMIZATION",
        command=run_optimization_pipeline,
        font=FontEngine.get("button")
    )
    optimize_btn.pack(fill="x", ipady=10)
    
    # Hand execution focus over to the main execution window loop thread
    app_window.show()

if __name__ == "__main__":
    bootstrap()
