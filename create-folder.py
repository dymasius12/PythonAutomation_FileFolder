from pathlib import Path

#create a folder
# Path('new_folder').mkdir()
# able in case if you have the folder
Path('new_folder').mkdir(exist_ok=True)

Path('new_folder/new_subfolder/new_subsubfolder').mkdir(parents=True, exist_ok=True)


