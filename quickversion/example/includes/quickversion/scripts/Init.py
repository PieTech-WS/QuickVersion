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
    if os.path.isfile("versions.qvcs"):
        log_session.error("此目录下已有QuickVersion版本文件.")
        raise QVersionInitERROR("DetectionERROR")
    try:
        if not Folder("./versions").is_empty():
            log_session.error("此目录下已有名为versions的文件夹且不为空.")
            raise QVersionInitERROR("DetectionERROR:Folder is not empty.")
        else:
            log_session.child_process("versions文件夹已存在.跳过..")
    except FolderNotFound:
        log_session.child_process("创建versions文件夹中..")
        os.mkdir("versions")
    with open("./config.qvcs", "w", encoding="utf-8") as a:
        log_session.child_process("创建配置文件confg.qvcs..")
        json.dump({}, a)
    with open("./versions.qvcs", "w", encoding="utf-8") as a:
        log_session.child_process("创建版本文件versions.qvcs..")
        json.dump({}, a)

