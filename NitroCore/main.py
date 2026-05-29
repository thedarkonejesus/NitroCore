"""
NitroCore Windows System Optimizer - Primary Application Entry Point.
"""

import os
import sys
import ctypes

# Dynamically ensure Python can locate the 'source' folder relative to main.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# UPDATED IMPORTS: Pointing to 'source' instead of 'src'
from source.utils.config import Config
from source.utils.lifecycle import LifecycleManager
from source.gui.window import Window
from source.gui.fonts import FontEngine
from source.gui.frame import CustomFrame
from source.gui.button import CustomButton
from source.gui.label import CustomLabel

def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

class NitroCoreApplication:
    """Manages the lifecycle, interface layout transitions, and Easter Egg states."""
    
    def __init__(self):
        self.app_window = None
        self.main_panel = None

    def draw_dashboard(self):
        """Assembles the visible components based on the active config state."""
        for widget in self.main_panel.canvas.winfo_children():
            widget.destroy()

        if Config.PI_BOY_MODE:
            bg_color = "#030803"
            fg_color = "#33ff33"
            self.app_window.canvas.configure(bg=bg_color)
            self.main_panel.canvas.configure(bg=bg_color)
            
            FontEngine.initialize()
            self._build_pipboy_layout(bg_color, fg_color)
        else:
            bg_color = "#202225"
            fg_color = "#F2F3F5"
            self._build_standard_layout(bg_color, fg_color)

    def _build_standard_layout(self, bg_color: str, fg_color: str):
        title_lbl = CustomLabel(
            parent=self.main_panel.canvas,
            text="System Optimization Dashboard",
            font=FontEngine.get("title")
        )
        title_lbl.configure(fg=fg_color, bg=bg_color)
        title_lbl.pack(anchor="w", pady=(0, 20))
        title_lbl.bind("<Button-1>", self._handle_secret_clicks)

        optimize_btn = CustomButton(
            parent=self.main_panel.canvas,
            text="RUN NITRO CORE OPTIMIZATION",
            command=lambda: print("[Engine] Running optimization pipeline..."),
            font=FontEngine.get("button")
        )
        optimize_btn.pack(fill="x", ipady=10)

    def _build_pipboy_layout(self, bg_color: str, fg_color: str):
        header_text = " ___________________________________________________________________________\n" \
                      "|  [STAT]    > [INV] <   [DATA]    [MAP]    [RADIO]   |  KALI CORE v4.0.0   |\n" \
                      "|_____________________________________________________|_____________________|"
        
        header_lbl = CustomLabel(self.main_panel.canvas, text=header_text, font=FontEngine.get("log"))
        header_lbl.configure(fg=fg_color, bg=bg_color, justify="left")
        header_lbl.pack(fill="x", pady=(0, 20))

        stats_box = CustomFrame(self.main_panel.canvas)
        stats_box.canvas.configure(bg=bg_color)
        stats_box.pack(fill="both", expand=True, pady=10)

        special_data = [
            ("S - STRENGTH", "10 [MAX]", ">> Carrying capacity optimized. Registry weight lifted."),
            ("P - PERCEPTION", "10 [MAX]", ">> File path scanning visibility at absolute maximum."),
            ("E - ENDURANCE", "10 [MAX]", ">> Process stamina verified. Handle exceptions absorbed."),
            ("C - CHARISMA", "10 [MAX]", ">> Network communication protocols fully persuasive."),
            ("I - INTELLIGENCE", "10 [MAX]", ">> Async worker thread memory allocation hyper-efficient."),
            ("A - AGILITY", "10 [MAX]", ">> UI update refresh latency dropped to zero ms."),
            ("L - LUCK", "10 [MAX]", ">> NullPointerErrors automatically avoided by fortune.")
        ]

        for idx, (stat, val, desc) in enumerate(special_data):
            row_text = f"{stat.ljust(16)} - {val}   {desc}"
            lbl = CustomLabel(stats_box.canvas, text=row_text, font=FontEngine.get("body"))
            lbl.configure(fg=fg_color, bg=bg_color, anchor="w")
            lbl.pack(fill="x", pady=4)

        purge_btn = CustomButton(
            parent=self.main_panel.canvas,
            text=">>>  [ INITIATE SYSTEM PURGE AND OVERCLOCK ]  <<<",
            command=lambda: print(">> [VATS] STARTING SYSTEM RAD PURGE MULTIPLIER..."),
            font=FontEngine.get("button")
        )
        purge_btn.configure(
            bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
            bd=2, relief="solid"
        )
        purge_btn.pack(fill="x", ipady=12, pady=(20, 0))

    def _handle_secret_clicks(self, event):
        Config.CLICK_COUNTER += 1
        if Config.CLICK_COUNTER >= 7:
            Config.PI_BOY_MODE = True
            ctypes.windll.kernel32.Beep(800, 150)
            self.app_window.canvas.title("PIP-BOY 3000 - ROB-CO INDUSTRIES")
            self.draw_dashboard()

    def run(self):
        Config.parse_arguments()

        if not is_admin():
            ctypes.windll.user32.MessageBoxW(
                0, "NitroCore requires Administrative Privileges to modify system registries.", "Access Denied", 0x10 | 0x0
            )
            sys.exit(0)

        LifecycleManager.enforce_single_instance()
        
        self.app_window = Window(title="NitroCore Windows Optimizer v1.0.0", width=950, height=650, resizable=False)
        FontEngine.initialize()
        
        self.main_panel = CustomFrame(self.app_window.canvas)
        self.main_panel.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.draw_dashboard()
        self.app_window.show()

if __name__ == "__main__":
    app = NitroCoreApplication()
    app.run()
