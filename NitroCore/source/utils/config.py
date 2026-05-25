"""Configuration utilities for loading and managing configurations"""

import json
import os
import yaml
from typing import Dict, Any, Optional
from pathlib import Path


class ConfigLoader:
    """Configuration loader supporting multiple formats"""
    
    @staticmethod
    def load_config(config_path: str) -> Dict[str, Any]:
        """Load configuration from file"""
        config_path = Path(config_path)
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
            
        with open(config_path, 'r') as f:
            if config_path.suffix.lower() == '.json':
                return json.load(f)
            elif config_path.suffix.lower() in ('.yml', '.yaml'):
                return yaml.safe_load(f)
            else:
                raise ValueError(f"Unsupported config format: {config_path.suffix}")
    
    @staticmethod
    def save_config(config: Dict[str, Any], output_path: str, format: str = 'json') -> None:
        """Save configuration to file"""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            if format.lower() == 'json':
                json.dump(config, f, indent=4)
            elif format.lower() in ('yml', 'yaml'):
                yaml.dump(config, f)
            else:
                raise ValueError(f"Unsupported output format: {format}")