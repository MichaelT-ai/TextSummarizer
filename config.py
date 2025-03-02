"""
Configuration management for TextSummarizer
"""
import os
import json
from typing import Dict, Any, Optional


class Config:
    """Configuration manager for TextSummarizer"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path or os.path.expanduser("~/.textsummarizer.json")
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        default_config = {
            "default_length": 200,
            "model": "gpt-3.5-turbo",
            "temperature": 0.5,
            "max_tokens": 150,
            "use_ai": True
        }
        
        if not os.path.exists(self.config_path):
            return default_config
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                loaded_config = json.load(f)
                # Merge with defaults
                default_config.update(loaded_config)
                return default_config
        except Exception as e:
            print(f"Warning: Could not load config file: {e}")
            return default_config
    
    def save_config(self) -> None:
        """Save current configuration to file"""
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save config file: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value"""
        self.config[key] = value
        self.save_config()