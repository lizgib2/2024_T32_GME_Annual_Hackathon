import os,sys
import numpy as np
import pandas as pd
import json

json_config_path = sys.argv[1]
parameters = json.load(json_config_path)

# Load in raw data
path_to_raw_data = parameters["1_preprocess_data"]["path_to_raw_data"]
loaded_raw_data = pd.read_csv(path_to_raw_data)

# Filter based on "maf" column values
maf_filter = parameters["1_preprocess_data"]["maf_filter"]
filtered_data = loaded_raw_data.loc[loaded_raw_data['maf'] > maf_filter]

# Write the filtered data to a new file
path_to_filtered_data = parameters["1_preprocess_data"]["path_to_filtered_data"]
filtered_data.write_csv(path_to_filtered_data)


