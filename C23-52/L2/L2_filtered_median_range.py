#C23-52, L2 filtered med range
#4/4/24

import csv

file_path = "C23-52/L2/L2_combined_summ_stats.csv"

# with open(file_path, "r") as file:
#     lines = file.readlines()

# lines[0] = "taxon" + lines[0]

# with open (file_path, 'w') as output_file:
#     output_file.writelines(lines)


#once csv has been edited import as dictionary
def csv_to_dict(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
    return data

file_path = "C23-52/L2/L2_combined_summ_stats.csv"
combined_ss_dict = csv_to_dict(file_path)

for entry in combined_ss_dict:
    if entry['taxon '] != ' ':
        taxonomy = entry['taxon '].split(';')[-1].strip()
        min_val = entry['min']
        max_val = entry['max']
        entry['range'] = f"{min_val}-{max_val}"

# now lets extract taxon, median, and range from the dict
extracted_data = []

for entry in combined_ss_dict:
    if entry['taxon '] != ' ':
        taxonomy = entry['taxon '].split(';')[-1].strip()
        median = entry['median']
        min_val = entry['min']
        max_val = entry['max']
        entry_range = f"{min_val}-{max_val}"
        extracted_data.append({'taxon': entry['taxon '], 'median': median, 'range': entry_range})

common_taxons = ['Firmicutes', 'Bacteroidetes', 'Fusobacteria', 'Other', 'Proteobacteria', 'Deferribacteres', 'Actinobacteria']

csv_file = "L2_filtered_median_range.csv"

# Limit the taxon strings to only common strings
for entry in extracted_data:
    entry['taxon'] = entry['taxon'].split(';p__')[-1]

# Filter the entries based on common taxons
filtered_median_range = []
for entry in extracted_data: 
    taxon = entry['taxon']
    if any(taxon.endswith(t) for t in common_taxons):
        filtered_entry = {
            'taxon': taxon,
            'median': entry['median'],
            'range': entry['range']
        }
        filtered_median_range.append(filtered_entry)

# Write the filtered data to CSV
fieldnames = ["taxon", "median", "range"]

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for entry in filtered_median_range:
        writer.writerow(entry)

print(f"Filtered taxonomy summary stats written to {csv_file}")