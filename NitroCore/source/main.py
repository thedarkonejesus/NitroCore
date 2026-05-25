import sys
import tkinter as tk
from tkinter import ttk
import threading
from src.modules.registry import RegistryOptimizer
from src.modules.temp_files import TempFileCleaner
from src.modules.disk_cleanup import DiskCleanup
from src.modules.services import ServiceManager
from src.modules.performance import PerformanceTuner

class GamingOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows Gaming Optimizer")
        self.root.geometry("600x500")
        
        # Create notebook tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tab pages
        self.create_registry_tab()
        self.create_temp_tab()
        self.create_disk_tab()
        self.create_performance_tab()
        self.create_status_tab()
        
        # Start optimization thread
        self.optimization_thread = threading.Thread(target=self.start_optimization, daemon=True)
        self.optimization_thread.start()
    
    def create_registry_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Registry")
        
        btn = ttk.Button(frame, text="Optimize Registry", command=self.optimize_registry)
        btn.pack(pady=20)
        
        self.registry_text = tk.Text(frame, height=10)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.registry_text.yview)
        self.registry_text.configure(yscrollcommand=scrollbar.set)
        
        self.registry_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def create_temp_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Temporary Files")
        
        btn = ttk.Button(frame, text="Clean Temp Files", command=self.clean_temp_files)
        btn.pack(pady=20)
        
        self.temp_text = tk.Text(frame, height=10)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.temp_text.yview)
        self.temp_text.configure(yscrollcommand=scrollbar.set)
        
        self.temp_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def start_optimization(self):
        """Start background optimization"""
        optimizer = RegistryOptimizer()
        cleaner = TempFileCleaner()
        disk = DiskCleanup()
        tuner = PerformanceTuner()
        
        # Run optimizations
        registry_results = optimizer.apply_all()
        temp_files = cleaner.clean_temp_directories()
        browser_cache = cleaner.clean_browser_cache()
        disk_cleanup = disk.clean_system_files()
        
        # Update status
        self.update_status("Optimization complete!")
    
    def update_status(self, message):
        """Update status messages"""
        self.status_text.insert(tk.END, f"{message}\n")
        self.status_text.see(tk.END)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = GamingOptimizerApp(root)
    app.run()