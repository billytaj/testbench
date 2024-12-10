import os
import sys
import time
from datetime import datetime as dt
import threading as th
import multiprocessing as mp
import testbench_helpers as help

#-----------------------------
#py testbench for test/perf bioinformatics tools.



if __name__ == "__main__":
    config_path = sys.argv[1]

    config_obj = help.tb_config(config_path)

    settings_dict = config_obj.get_settings_dict()
    inputs_dict = config_obj.get_inputs_dict
    tools_dict = config_obj.get_tools_dict

    tb_obj = help.tb_capsule(settings_dict, inputs_dict, tools_dict)
        