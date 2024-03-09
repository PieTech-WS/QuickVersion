import json
import os
import inspect


class Module:
    def check(self):
        with open("private/dynmodule.json", "r") as a:
            dynmodules: dict = json.load(a)
        frame = inspect.currentframe().f_back
        caller_file = frame.f_code.co_filename
        path = caller_file.replace("{}/".format(os.path.abspath(".")), "")
        if path not in dynmodules.keys():
            return "None"
        else:
            return dynmodules[path]
