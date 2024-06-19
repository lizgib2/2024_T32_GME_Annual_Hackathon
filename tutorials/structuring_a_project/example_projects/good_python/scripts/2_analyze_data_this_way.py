import os,sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

import this.analysis

# Load json file specified as the first command line argument
json_config_path = sys.argv[1]
parameters = json.load(json_config_path)

# Write the filtered data to a new file
path_to_filtered_data = parameters["1_preprocess_data"]["path_to_filtered_data"]
filtered_data = pd.read_csv(path_to_filtered_data)

# Analyze the data "this" way
analysis_output = this.analysis(filtered_data)

# Make plot of analysis results and save it
path_to_plots_directory = parameters["2_analyze_data_this_way"]["path_to_plots_directory"]
plt.plot(analysis_output)
plt.savefig(os.path.join(path_to_plots_directory, "this.png"))
