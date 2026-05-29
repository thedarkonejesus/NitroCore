import json
from pathlib import Path
from typing import Dict, Any, Union
import yaml

class ConfigLoader:
    """
    High-performance, fault-tolerant configuration loader 
    supporting JSON and YAML with automatic schema fallbacks.
    """
    
    # Global hardcoded app fallback defaults to guarantee the UI never boots broken
    DEFAULT_CONFIG = {
        "theme": "dark",
        "auto_clean_on_launch": False,
        "retention_days": 30,
        "enabled_modules": {
            "registry": True,
            "temp_files": True,
            "disk_cleanup": True,
            "services": True,
            "performance": True
        }
    }

    @classmethod
    def load_config(cls, config_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Loads configuration from a file. If the file is missing or corrupted,
        it automatically safely falls back to default settings without crashing the app.
        """
        target_path = Path(config_path)
        
        # If no config exists yet, gracefully generate a default template file
        if not target_path.exists():
            cls.save_config(cls.DEFAULT_CONFIG, target_path, format=target_path.suffix.strip('.'))
            return cls.DEFAULT_CONFIG.copy()
            
        try:
            with open(target_path, 'r', encoding='utf-8') as f:
                file_ext = target_path.suffix.lower()
                
                if file_ext == '.json':
                    data = json.load(f)
                elif file_ext in ('.yml', '.yaml'):
                    data = yaml.safe_load(f)
                else:
                    raise ValueError(f"Unsupported config format: {file_ext}")
                    
                # Handle the case where a file exists but is completely empty
                if data is None:
                    return cls.DEFAULT_CONFIG.copy()
                    
                # Merge loaded data on top of defaults to guarantee missing keys don't cause KeyErrors
                merged_config = cls.DEFAULT_CONFIG.copy()
                if isinstance(data, dict):
                    merged_config.update(data)
                return merged_config
                
        except (json.JSONDecodeError, yaml.YAMLError, PermissionError) as e:
            # Print to console for developers, but recover gracefully for the user
            print(f"[Warning] Configuration corrupted or unreadable ({e}). Loading fail-safe defaults.")
            return cls.DEFAULT_CONFIG.copy()

    @classmethod
    def save_config(cls, config: Dict[str, Any], output_path: Union[str, Path], format: str = 'json') -> None:
        """
        Saves application configurations to disk safely, 
        ensuring parent directory trees are initialized cleanly.
        """
        target_path = Path(output_path)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        save_format = format.lower().strip('.')
        
        try:
            with open(target_path, 'w', encoding='utf-8') as f:
                if save_format == 'json':
                    json.dump(config, f, indent=4, ensure_ascii=False)
                elif save_format in ('yml', 'yaml'):
                    yaml.dump(config, f, default_flow_style=False, sort_keys=False)
                else:
                    raise ValueError(f"Unsupported output format: {format}")
        except Exception as e:
            print(f"[Error] Failed to write configuration to disk: {e}")
