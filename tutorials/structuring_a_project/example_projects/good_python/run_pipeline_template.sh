# Path to the folder containing your scripts
path_to_scripts="/.../good_python/scripts"

# Path to config file with parameters you want to run
path_to_config_file="path_to_config_file_of_interest"

# Step 1: Run preprocessing
python $path_to_scripts/1_preprocess_data.py $path_to_config_file

# Step 2: Run "this" analysis
python $path_to_scripts/2_analyze_data_that_way.py $path_to_config_file

# Step 3: Run "that" analysis
python $path_to_scripts/2_analyze_data_this_way.py $path_to_config_file
