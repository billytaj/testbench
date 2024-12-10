import configparser as conf
import os
import sys
import threading as th
import subprocess as sp
import multiprocessing as mp
#-----------------------------------------
# helper classes for testbench.

#--------------------------------------------------------------
#job handler
class tb_capsule:
    def __init__(self, settings_dict, inputs_dict, tools_dict):

        self.settings_dict = settings_dict
        self.inputs_dict = inputs_dict
        self.tools_dict = tools_dict




#---------------------------------------------------------------
#config handler
class tb_config:
    def __init__(self, config_path):
        self.config_obj = conf.ConfigParser()
        self.config_read = self.config_obj.read(config_path)
        self.tools_dict = dict()
        self.settings_dict = dict()
        self.inputs_dict = dict()
        #generic settings for whatever
        if("settings" in self.config_read):
            settings_config = self.config_read["settings"]
            
            if("export_dir" in settings_config):
                self.settings_dict["export_dir"] = str(settings_config["export_dir"])

        #expecting input files <which will be different reads> be listed in the config as numbers
        if("inputs" in self.config_read):
            
            input_config = self.config_read["inputs"]
            input_list = sorted(input_config.keys())
            for item in input_list:
                self.inputs_dict[item] = input_config[item]

        #expecting toolpaths to be tagged with their names
        if("tools" in self.config_read):
            tools_config = self.config_read["tools"] 
            tool_list = sorted(tools_config.keys())
            for item in tool_list:
                self.tools_dict[item] = str(tools_config[item])
    

    def get_settings_dict(self):
        return self.settings_dict
    
    def get_inputs_dict(self):
        return self.inputs_dict
    
    def get_tools_dict(self):
        return self.tools_dict
