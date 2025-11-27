from util.json_file_manager import JSONFileManager
from util.params import Params

import pathlib as path

class JSONReader:
    def __init__(self, file_name: str):
        self.file_path = path.Path(__file__).parent.parent / 'params' / file_name
        self.JSONFileManager = JSONFileManager(self.file_path)
        self.json_file = self.JSONFileManager.readJSON()
    
        if type(self.json_file) is not dict or ('velocity' not in self.json_file or  'theta' not in self.json_file or 'azimuthal_angle' not in self.json_file or 'g' not in self.json_file or 't_start' not in self.json_file or 't_end' not in self.json_file or 'x0' not in self.json_file or 'y0' not in self.json_file or 'z0' not in self.json_file):
            print("One of the keys are not correctly formatted or present. Using default data")
            self.json_file = {
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
        self.params = Params(self.json_file['velocity'], self.json_file['theta'], self.json_file['azimuthal_angle'], self.json_file['g'], self.json_file['t_start'], self.json_file['t_end'], self.json_file['x0'], self.json_file['y0'], self.json_file['z0'])
        



def main():
    file_name = 'ex1.json'
    reader = JSONReader(file_name)
    reader.params.print_all()


if __name__ == "__main__":
    main()