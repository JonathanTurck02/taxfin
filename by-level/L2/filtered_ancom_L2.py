import csv

ANCOMBC_dict = {}

with open("ds3_PLE_vs_HC/ANCOMBC/L2_phylum.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        taxon = row[0]
        pvalue = float(row[8])
        qvalue = float(row[10])

        ANCOMBC_dict[taxon] = {'p_GroupPLE': pvalue, 'q_GroupPLE': qvalue}


# print(ANCOMBC_dict)
        
new_ANCOMBC_dict = {}

# Iterate over the keys of the ANCOMBC_dict and remove 'p__' from each key
for taxon, values in ANCOMBC_dict.items():
    # Remove 'p__' from the taxon entry and strip any leading or trailing spaces
    new_taxon = taxon.replace('p__', '').strip()
    # Add the entry with the modified taxon name to the new dictionary
    new_ANCOMBC_dict[new_taxon] = values

# print(new_ANCOMBC_dict)
    
common_taxons = ['Proteobacteria', 'Desulfobacterota', 'Firmicutes_C', 'Firmicutes_A', 'Campylobacterota', 'Firmicutes', 'Cyanobacteria', 'Bacteroidota', 'Firmicutes_B', 'Fusobacteriota', 'Actinobacteriota']

filtered_data_dict = {}

for taxon, values in new_ANCOMBC_dict.items():
    if taxon in common_taxons:
        filtered_data_dict[taxon] = values

with open('filtered_ANCOMBC.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['taxon', 'p_GroupPLE', 'q_GroupPLE'])
    # Write the data rows
    for taxon, values in filtered_data_dict.items():
        csvwriter.writerow([taxon, values['p_GroupPLE'], values['q_GroupPLE']])
