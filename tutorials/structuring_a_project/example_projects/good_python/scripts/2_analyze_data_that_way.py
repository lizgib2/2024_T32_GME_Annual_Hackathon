import os,sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import that.analysis

# Write the filtered data to a new file
path_to_filtered_data = "path to filtered data"
filtered_data = pd.read_csv(path_to_filtered_data)

# Analyze the data "that" way
analysis_output = that.analysis(filtered_data)

# Make plot of analysis results and save it
path_to_plots_directory = "path to plots directory"
plt.plot(analysis_output)
plt.savefig(os.path.join(path_to_plots_directory, "that.png"))