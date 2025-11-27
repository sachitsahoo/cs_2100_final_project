from util.json_file_manager import JSONFileManager
from util.params import Params

import pathlib as path
import json

class JSONWriter:
    def __init__(self, file_name: str, params: Params):
        self.file_path = path.Path(__file__).parent.parent / 'params' / file_name
        self.JSONFileManager = JSONFileManager(self.file_path)
        self.json_file = self.JSONFileManager.writeJSON(params)

        



def main():
    file_name = "ex2.json"
    params = Params(5.0, 46.0, 0.0, 9.81, 0, 3, 0, 1, 0)
    writer = JSONWriter(file_name, params)
    with path.Path("./params/" + file_name).open() as f:
        print(json.load(f))


if __name__ == "__main__":
    main()