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

    