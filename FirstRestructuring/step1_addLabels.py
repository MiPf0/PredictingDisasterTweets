import os

dir_path = 'C:/Users/micha/Documents/BScThesis/data_crisisnlp_r17_events_all_pre'

for subdir in os.listdir(dir_path):
    subdir_path = os.path.join(dir_path, subdir)
    
    if os.path.isdir(subdir_path):
        event_name = subdir[:-5]
        if 'earthquake' in subdir:
            event_type_label = 'earthquake'
        elif 'floods' in subdir:
            event_type_label = 'floods'
        elif 'hurricane' in subdir or 'cyclone' in subdir:
            event_type_label = 'hurricane'
        elif 'wildfires' in subdir:
            event_type_label = 'wildfires'
        else:
            event_type_label = 'unknown'

        for file_name in os.listdir(subdir_path):
            if file_name.endswith('.tsv'):
                file_path = os.path.join(subdir_path, file_name)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                new_lines = []
                for i, line in enumerate(lines):
                    line = line.strip()
                    if i == 0:
                        new_line = 'event_name_label\tevent_type_label\t{}'.format(line)
                    else:
                        new_line = '{}\t{}\t{}'.format(event_name, event_type_label, line)
                    new_lines.append(new_line)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(new_lines))