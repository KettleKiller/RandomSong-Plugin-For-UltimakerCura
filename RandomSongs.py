import os
import random
from ..Script import Script


class RandomSongs(Script):
    """Selects a random song from a folder and plays it when the printing ends.
    """

    def getSettingDataString(self):
        return """{
            "name": "Random Song",
            "key": "RandomSong",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "Enabled":
                {
                    "label": "Enabled",
                    "description": "When enabled, final gcode will have a song at the end",
                    "type": "bool",
                    "default_value": false
                }
            }
        }"""

    def execute(self, data):

        if self.getSettingValueByKey("Enabled"):

            filetoplay=""
            folder = os.path.join(os.path.expanduser("~"), "OneDrive", "Documentos", "UltimakerGcodesongs")

            if not os.path.exists(folder):
                os.makedirs(folder)
            gsong_files = [f for f in os.listdir(folder) if f.endswith('.gsong')]
            if gsong_files:
                filetoplay = random.choice(gsong_files)
            else:
                data[-1] += f"\n;Sin archivos musicales en {folder}\n"
                data[-1] += "\n"
                return data

            songdir = os.path.join(folder, filetoplay)
            m300_lines = []
            with open(songdir, 'r') as file:
                for line in file:
                    if line.startswith("M300") or line.startswith("G4"):
                        m300_lines.append(line.strip())

            if m300_lines:
                data[-1] += f"\n ;Gsong to play: {filetoplay} \n" + "\n".join(m300_lines) + "\n"
            else:
                data[-1] += f"\n; {filetoplay} Archivo musical sin M300 ni G4 \n"

        data[-1] += "\n"
        return data
