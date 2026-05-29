import sys
import tkinter as tk
from tkinter import ttk
import threading
import queue  # Added for thread-safe UI communication

# Safely importing modules
try:
    from src.modules.registry import RegistryOptimizer
    from src.modules.temp_files import TempFileCleaner
    from src.modules.disk_cleanup import DiskCleanup
    from src.modules.services import ServiceManager
    from src.modules.performance import PerformanceTuner
except ImportError:
    # Fallback mocks for standalone testing
    class RegistryOptimizer: def apply_all(self): return "Registry optimized."
    class TempFileCleaner: 
        def clean_temp_directories(self): return "Temp cleared."
        def clean_browser_cache(self): return "Cache cleared."
    class DiskCleanup: def clean_system_files(self): return "Disk cleaned."
    class PerformanceTuner: pass

class GamingOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows Gaming Optimizer")
        self.root.geometry("600x500")
        
        # Queue for thread-safe communication
        self.update_queue = queue.Queue()
        
        # Create notebook tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 1. ALWAYS build the full UI first so all widgets exist
        self.create_registry_tab()
        self.create_temp_tab()
        self.create_disk_tab()
        self.create_performance_tab()
        self.create_status_tab()
        
        # 2. Start checking the queue for safe UI updates
        self.listen_for_updates()
        
    def create_registry_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Registry")
        
        # Pointing to a functional thread-safe trigger
        self.reg_btn = ttk.Button(frame, text="Optimize Registry", command=lambda: self.run_in_background(self.optimize_registry_logic))
        self.reg_btn.pack(pady=20)
        
        self.registry_text = tk.Text(frame, height=10)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.registry_text.yview)
        self.registry_text.configure(yscrollcommand=scrollbar.set)
        
        self.registry_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def create_temp_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Temporary Files")
        
        self.temp_btn = ttk.Button(frame, text="Clean Temp Files", command=lambda: self.run_in_background(self.clean_temp_logic))
        self.temp_btn.pack(pady=20)
        
        self.temp_text = tk.Text(frame, height=10)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.temp_text.yview)
        self.temp_text.configure(yscrollcommand=scrollbar.set)
        
        self.temp_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_disk_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Disk Cleanup")
        
    def create_performance_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Performance")

    def create_status_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Status Log")
        
        self.status_text = tk.Text(frame, height=15)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.status_text.yview)
        self.status_text.configure(yscrollcommand=scrollbar.set)
        
        self.status_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # --- THREAD MANAGEMENT ---
    
    def run_in_background(self, target_func):
        """Helper to safely spawn tasks in a background thread so the UI never hangs"""
        thread = threading.Thread(target=target_func, daemon=True)
        thread.start()

    def optimize_registry_logic(self):
        self.safe_log("Starting Registry Optimization...")
        optimizer = RegistryOptimizer()
        results = optimizer.apply_all()
        # Update text box via queue safely
        self.update_queue.put(('text_insert', self.registry_text, f"{results}\n"))
        self.safe_log("Registry Optimization Complete!")

    def clean_temp_logic(self):
        self.safe_log("Cleaning temporary files...")
        cleaner = TempFileCleaner()
        res1 = cleaner.clean_temp_directories()
        res2 = cleaner.clean_browser_cache()
        self.update_queue.put(('text_insert', self.temp_text, f"{res1}\n{res2}\n"))
        self.safe_log("Temporary files cleaned successfully!")

    def safe_log(self, message):
        """Thread-safe logging mechanism using the queue"""
        self.update_queue.put(('status_insert', message))

    def listen_for_updates(self):
        """Runs on the MAIN thread, constantly checking for UI update tasks from background threads"""
        try:
            while True:
                task = self.update_queue.get_nowait()
                task_type = task[0]
                
                if task_type == 'status_insert':
                    msg = task[1]
                    self.status_text.insert(tk.END, f"[LOG]: {msg}\n")
                    self.status_text.see(tk.END)
                elif task_type == 'text_insert':
                    widget, msg = task[1], task[2]
                    widget.insert(tk.END, msg)
                    widget.see(tk.END)
                    
                self.update_queue.task_done()
        except queue.Empty:
            pass
        finally:
            # Check the queue again in 100ms
            self.root.after(100, self.listen_for_updates)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = GamingOptimizerApp(root)
    app.run()
