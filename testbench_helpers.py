import configparser as conf
import os
import sys

#-----------------------------------------
# helper classes for testbench.


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
            
    

    def get_settings_dict(self):
        return self.settings_dict
    
    def get_inputs_dict(self):
        return self.inputs_dict
    
    def get_tools_dict(self):
        return self.tools_dict
