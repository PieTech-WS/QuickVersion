import json
import os
from ..Crash.qversion_init import QVersionInitERROR
from ...coraos.log import console
from ...coraos.fs.folder import Folder, FolderNotFound


def init():
    log_session = console.Log()
    
    log_session.process("开始初始化QuickVersion文件")
    log_session.child_process("检查中")
    if os.path.isfile("config.qvcs"):
        log_session.error("此目录下已有QuickVersion配置文件.")
        raise QVersionInitERROR("DetectionERROR")
    try:
        if Folder("./versions").is_empty():
            log_session.error("此目录下已有名为versions的文件夹.")
            raise QVersionInitERROR("DetectionERROR")
    except FolderNotFound:
        
    with open("./versions.qvcs", "r", encoding="utf-8") as a:
        json.dump({}, a)
    os.mkdir("./versions")
    
