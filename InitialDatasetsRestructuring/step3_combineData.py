import os
import csv

root_dir = 'C:/Users/micha/Documents/BScThesis/data_crisisnlp_r17_events_all_post'

for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    
    if os.path.isdir(folder_path):
        merged_file_name = folder + '_merged.tsv'
        merged_file_path = os.path.join(folder_path, merged_file_name)
        
        header = None
        data = []
        
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            
            if os.path.isfile(file_path):
                
                with open(file_path, 'r', encoding='utf-8') as tsv_file:
                    tsv_reader = csv.reader(tsv_file, delimiter='\t')
                    
                    if header is None:
                        header = next(tsv_reader)
                    
                    for row in tsv_reader:
                        if row != header:
                            data.append(row)
                        
                os.remove(file_path)
        
        with open(merged_file_path, 'w', newline='', encoding='utf-8') as merged_file:
            tsv_writer = csv.writer(merged_file, delimiter='\t')
            
            tsv_writer.writerow(header)
            
            for row in data:
                if row != header:
                    tsv_writer.writerow(row)
