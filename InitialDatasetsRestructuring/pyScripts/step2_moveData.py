import os
import shutil

naming_datasets = ['dev', 'train', 'test']

naming_tsv_ending = '.tsv'

source_dir = 'C:/Users/micha/Documents/BScThesis/data_crisisnlp_r17_events_all_pre'
destination_dir = 'C:/Users/micha/Documents/BScThesis/data_crisisnlp_r17_events_all_post/'

for root, dirs, files in os.walk(source_dir):
    for file_name in files:
        for dataset_name in naming_datasets:
            if file_name.endswith(dataset_name + naming_tsv_ending):
                source_file_path = os.path.join(root, file_name)
                destination_file_path = os.path.join(destination_dir + dataset_name, file_name)
                shutil.move(source_file_path, destination_file_path)