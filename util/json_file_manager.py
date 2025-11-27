import json
import pathlib as path
from util.params import Params

class JSONFileManager:
    def __init__(self, file_path: str):
        self.file_path_str = file_path
        self.file_path_obj = path.Path(self.file_path_str)
        

    def readJSON(self):
        if self.file_path_obj.exists():
            with self.file_path_obj.open() as f:
                return json.load(f)

        self.file_path_obj.parent.mkdir(parents=True, exist_ok=True)

        default_data = {
            "velocity": 10.0,
            "theta": 0.0,
            "azimuthal_angle": 0.0,
            "g": 9.81,
            "t_start": 0.0,
            "t_end": 3.0,
            "x0": 0.0,
            "y0": 0.0,
            "z0": 0.0
        }

        self.file_path_obj.write_text(json.dumps(default_data, indent=4))



        with self.file_path_obj.open() as f:
            return json.load(f)
        
    def writeJSON(self, params: Params) -> None:
        self.file_path_obj.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "velocity": params.velocity,
            "theta": params.theta,
            "azimuthal_angle": params.azimuthal_angle,
            "g": params.g,
            "t_start": params.t_start,
            "t_end": params.t_end,
            "x0": params.x0,
            "y0": params.y0,
            "z0": params.z0
        }

        self.file_path_obj.write_text(json.dumps(data, indent=4))