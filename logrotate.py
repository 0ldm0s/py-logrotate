# -*- coding: UTF-8 -*-
import os
import orjson as json
from logging.handlers import RotatingFileHandler
from typing import List, Union, Dict

cmd: str = "pm2 jlist"
result = os.popen(cmd)
jlist: str = str(result.read())
jdata: List[Union[List, Dict]] = json.loads(jlist)
for _conf_ in jdata:
    err_log: str = _conf_["pm2_env"]["pm_err_log_path"]
    out_log: str = _conf_["pm2_env"]["pm_out_log_path"]
    pm_id: int = _conf_["pm2_env"]["pm_id"]
    need_restart: bool = False
    if os.path.isfile(err_log) and os.path.getsize(err_log) >= 10485760:
        print(f"now rotating:[{err_log}]")
        err_log_handler = RotatingFileHandler(
            err_log, maxBytes=10485760, backupCount=10)
        err_log_handler.doRollover()
        need_restart = True
    if os.path.isfile(out_log) and os.path.getsize(out_log) >= 10485760:
        print(f"now rotating:[{out_log}]")
        out_log_handler = RotatingFileHandler(
            out_log, maxBytes=10485760, backupCount=10)
        out_log_handler.doRollover()
        need_restart = True
    if need_restart:
        os.system(f"pm2 reload {pm_id}")
