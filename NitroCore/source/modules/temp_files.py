import tempfile
import shutil
import os

class TempFileCleaner:
    def __init__(self):
        self.paths_to_clean = [
            os.path.expandvars('%TEMP%'),
            os.path.expandvars('%LOCALAPPDATA%\\Temp'),
            os.path.expandvars('%SYSTEMROOT%\\Temp')
        ]
    
    def clean_temp_directories(self):
        """Clean all temporary directories"""
        cleaned_files = []
        for path in self.paths_to_clean:
            if os.path.exists(path):
                for root, dirs, files in os.walk(path):
                    for f in files:
                        try:
                            os.remove(os.path.join(root, f))
                            cleaned_files.append(os.path.join(root, f))
                        except PermissionError:
                            pass
        return cleaned_files
    
    def clean_browser_cache(self):
        """Clean browser cache files"""
        browser_paths = {
            'Chrome': '%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cache',
            'Firefox': '%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cache2'
        }
        
        cleaned_files = []
        for browser, path in browser_paths.items():
            expanded_path = os.path.expandvars(path)
            for root, dirs, files in os.walk(expanded_path):
                for f in files:
                    try:
                        os.remove(os.path.join(root, f))
                        cleaned_files.append(os.path.join(root, f))
                    except (PermissionError, FileNotFoundError):
                        pass
        return cleaned_files