from recbole.quick_start import run_recbole
import json
from time import time

def run_configurations(model):
    # Run the RecBole model with specified configurations
    output_dict = run_recbole(model=model, config_file_list=["config_test.yaml"])
    

run_configurations("SimpleX")
run_configurations("BPR")
