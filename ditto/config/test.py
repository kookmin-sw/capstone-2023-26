import os
current_dir = os.path.abspath(__file__)
target_dir = os.path.dirname(current_dir) + '/videostorage'
folder_path = target_dir
ts_files = [f for f in os.listdir(folder_path) if f.endswith(".ts")]
ts_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
ts_file_paths = [os.path.abspath(os.path.join(folder_path, f)) for f in ts_files]

print(ts_file_paths)