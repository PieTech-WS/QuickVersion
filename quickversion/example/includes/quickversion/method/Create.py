import os
from ...coraos.fs.folder import Folder
from ...coraos.data.json.DataStorage import DStorage


def channel(name: str):
    versions_folder = Folder("./versions")
    versions_folder.new_child_folder(name)
    versions_file = DStorage("./versions.qvcs", True)
    versions_file.newKey(name)
