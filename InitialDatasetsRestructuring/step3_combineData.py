import os
import csv

# Define the root directory where your subfolders are located
root_dir = 'C:/Users/micha/Documents/BScThesis/data_crisisnlp_r17_events_all_post'

# Loop through each subfolder
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    
    # If the item in the root directory is a directory (i.e., not a file)
    if os.path.isdir(folder_path):
        
        # Define the merged file name for this subfolder
        merged_file_name = folder + '_merged.tsv'
        merged_file_path = os.path.join(folder_path, merged_file_name)
        
        # Initialize the header row for the merged file
        header = None
        
        # Initialize the list to store all rows of data from the individual tsv files
        data = []
        
        # Loop through each tsv file in the subfolder
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            
            # If the item in the subfolder is a file (i.e., not a directory)
            if os.path.isfile(file_path):
                
                # Open the tsv file and read the data
                with open(file_path, 'r', encoding='utf-8') as tsv_file:
                    tsv_reader = csv.reader(tsv_file, delimiter='\t')
                    
                    # If this is the first file being read, save the header row
                    if header is None:
                        header = next(tsv_reader)
                    
                    # Loop through each row of data in the tsv file and save it to the data list
                    for row in tsv_reader:
                        # Skip over any rows that match the header row
                        if row != header:
                            data.append(row)
                        
                # Delete the individual tsv file
                os.remove(file_path)
        
        # Write the merged data to a new tsv file
        with open(merged_file_path, 'w', newline='', encoding='utf-8') as merged_file:
            tsv_writer = csv.writer(merged_file, delimiter='\t')
            
            # Write the header row
            tsv_writer.writerow(header)
            
            # Write the data rows, skipping over any rows that match the header row
            for row in data:
                if row != header:
                    tsv_writer.writerow(row)
