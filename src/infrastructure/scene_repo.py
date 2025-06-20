import json
import os
from typing import List, Dict


class SceneRepository:

    @staticmethod
    def load_scenes(file_path: str = "data/scenes.json") -> List[Dict[str, str]]:
        if not os.path.exists(file_path):
            print(f"❌ Sahne dosyası bulunamadı: {file_path}")
            return []

        with open(file_path, "r", encoding="utf-8") as f:
            try:
                scenes = json.load(f)
                return scenes
            except json.JSONDecodeError as e:
                print(f"🚫 JSON okuma hatası: {e}")
                return []
