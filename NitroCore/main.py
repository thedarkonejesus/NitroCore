"""
NitroCore Windows System Optimizer - Primary Application Entry Point.
Handles administrative elevation checking, kernel mutex enforcement, 
emergency process teardowns, high-DPI font compiling, and the GUI loop.
"""

import sys
import ctypes
from src.utils.lifecycle import LifecycleManager
from src.gui.window import Window
from src.gui.fonts import FontEngine
from src.gui.frame import CustomFrame
from src.gui.button import CustomButton
from src.gui.label import CustomLabel

def is_admin() -> bool:
    """
    Validates if the active process context has administrative rights.
    Ensures low-level Win32 service and registry edits won't crash on execution.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

def app_emergency_shutdown():
    """Triggered automatically via atexit if the process terminates abruptly."""
    print("[Shutdown] Releasing open system hooks, logs, and handles safely.")
    # Low-level system cleanup hooks go here

def run_optimization_pipeline():
    """Placeholder trigger showing how background workers are invoked."""
    print("[Engine] Dispatched asynchronous system optimization tasks...")

def bootstrap():
    """Validates runtime environment, enforces safeguards, and builds the visual canvas."""
    # 1. Enforce administrative privilege limits immediately at startup
    if not is_admin():
        # Present a native Win32 error dialog before any framework engine boots
        ctypes.windll.user32.MessageBoxW(
            0, 
            "NitroCore requires Administrative Privileges to modify system registries and services.\n\nPlease relaunch your terminal or executable as an Administrator.", 
            "Access Denied - Elevation Required", 
            0x10 | 0x0  # MB_ICONERROR | MB_OK Windows API hex flags
        )
        sys.exit(0)

    # 2. Enforce single-instance mutex limits to prevent parallel registry conflicts
    LifecycleManager.enforce_single_instance()
    
    # 3. Bind emergency exiting routines
    LifecycleManager.register_emergency_cleanup(app_emergency_shutdown)
    
    # 4. Spawn primary high-DPI dark-themed workspace window manager
    app_window = Window(
        title="NitroCore Windows Optimizer v1.0.0",
        width=950,
        height=650,
        resizable=False
    )
    
    # 5. Spin up the hardware font engine inside the active Tkinter window context
    FontEngine.initialize()
    
    # 6. Assemble your dashboard panels cleanly using your custom UI classes
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
