import os,sys
import numpy as np
import pandas as pd

# Load in raw data
path_to_raw_data = "path to raw data"
loaded_raw_data = pd.read_csv(path_to_raw_data)

# Filter based on "maf" column values
maf_filter = 0.05
filtered_data = loaded_raw_data.loc[loaded_raw_data['maf'] > maf_filter]

# Write the filtered data to a new file
path_to_filtered_data = "path to filtered data"
filtered_data.write_csv(path_to_filtered_data)


