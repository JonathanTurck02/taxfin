import csv

file_path = "combined_summ_stats.csv"

with open(file_path, "r") as file:
    lines = file.readlines()

lines[0] = "taxon" + lines[0]

with open (file_path, 'w') as output_file:
    output_file.writelines(lines)


#once csv has been edited import as dictionary

def csv_to_dict(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
    return data

file_path = "combined_summ_stats.csv"
combined_ss_dict = csv_to_dict(file_path)

# print(combined_ss_dict)

for entry in combined_ss_dict:
    if entry['taxon '] != ' ':
        taxonomy = entry['taxon '].split(';')[-1].strip()
        min_val = entry['min']
        max_val = entry['max']
        entry['range'] = f"{min_val}-{max_val}"

# print(combined_ss_dict)

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

# print(extracted_data)

# Define common_taxons
common_taxons = ['Anaerococcus', 'Collinsella', 'Anaerofilum', 'CAG-462', 'Massilistercora', 'Fusicatenibacter', 'Leuconostoc', 'CAG-521', 'Sutterella', 'Actinomyces', 'Fournierella', 'Odoribacter', 'Ruminococcus_A', '1XD42-69', 'Ileibacterium', 'Fusobacterium_B', 'Nocardioides', 'Massilioclostridium', 'Phocaeicola', 'Mediterraneibacter', 'Prevotellamassilia', 'Clostridioides_A', 'Listeria', 'Porphyromonas', 'Catenibacterium', 'CAG-279', 'Muribaculum', 'Romboutsia', 'Fusobacterium_C', '[Anaeroplasmataceae_Juniper_p2_metabat2_high_PE.004.contigs]', 'Bilophila', 'Lactonifactor', 'Holdemanella', 'Ruminococcus_B', 'Lancefieldella', 'Bacillus_AO', 'Bulleidia', 'Massilimaliae', 'Planococcus', 'Faecalicoccus', 'Helicobacter_A', 'VUNI01', 'Eggerthella', 'Muricomes', 'Allisonella', 'Agathobacter', 'Christensenella', 'Paraprevotella', 'Mogibacterium', '[Erysipelatoclostridiaceae_Garnier_p1_maxbin2_low_prob.015.contigs]', 'Acidaminococcus', 'TF01-11', '[Erysipelatoclostridiaceae_Snoopy_p2_metabat2_low_PE.005.contigs]', 'Dubosiella', 'Schaedlerella', 'Streptomyces', 'Pauljensenia', 'Parabacteroides', 'Gordonibacter', 'Staphylococcus', 'Ruminococcus_D', 'Bittarella', 'Olsenella_E', 'Fusobacterium', '[Atopobiaceae_Jenna_p2_metabat2_low_PE.018.contigs]', 'Alterileibacterium', 'Butyricimonas', 'Peptoniphilus_A', 'Bariatricus', 'Acetatifactor', 'Lactococcus_A', 'Marseille-P3106', 'Agathobaculum', 'NSJ-62', 'Flavobacterium', 'Frondihabitans', 'Butyricicoccus', 'Trichormus', 'Enorma', 'Cetobacterium_A', 'Microbacterium', 'Acetivibrio_A', 'Criibacterium', 'Lacticaseibacillus', 'Cutibacterium', 'Beduini', 'Peptacetobacter', 'Lachnoclostridium_A', 'Clostridium_AP', 'Gemella', 'Rikenella', 'Citrobacter', 'Finegoldia', 'Phascolarctobacterium_A', 'Clostridium_L', 'Enterococcus_B', 'Paraeggerthella', 'Harryflintia', 'Helicobacter_D', 'Streptococcus', 'Catenibacillus', 'Brevundimonas', 'Emergencia', 'Dialister', 'Faecalibacterium', 'Pontibacillus', 'Senegalimassilia', 'Cellulosilyticum', 'Slackia_A', 'CAG-81', 'Ruminococcus_C', 'Allobaculum', 'CAG-127', 'Clostridium_J', 'Olsenella', 'Anaerotignum', 'Ellagibacter', 'Pediococcus', 'RC9', 'Blautia_A', 'Intestinimonas', 'Vagococcus_A', 'Roseburia', 'Faecalitalea', 'Flavonifractor', 'An7', 'Anaerosacchariphilus', 'UMGS1590', 'Faecalibacillus', 'Prevotella', 'Variovorax', 'Eubacterium_J', 'Hespellia', 'Anaerobutyricum', 'Levilactobacillus', 'Clostridioides', 'UBA9475', 'Dwaynesavagella', '28L', 'GCA-900066495', 'Hungatella', 'UBA9502', 'Lachnoclostridium_B', 'Alistipes', 'Bifidobacterium', 'Dorea_B', 'Helicobacter_B', 'Butyrivibrio_A', 'Eubacterium_M', 'UBA1191', 'Stoquefichus', 'Peptostreptococcus', 'Phascolarctobacterium', 'Enterocloster', 'Merdimonas', 'Niameybacter', 'An92', 'Desulfovibrio', 'Megamonas', 'Porphyromonas_A', 'Extibacter', 'Ruthenibacterium', 'Intestinibacter', 'BX12', 'Pseudoruminococcus', 'Vagococcus', 'Faecalimonas', 'Clostridium_R', 'Enterococcus_E', 'Corynebacterium', 'Campylobacter_D', 'Latilactobacillus', 'Bacillus_J', 'Lactococcus', '14-2', 'Holdemania', 'Gordonia', 'Clostridium_Q', 'Marvinbryantia', 'Negativibacillus', 'Fusobacterium_A', 'Adlercreutzia', 'Clostridium', 'Lacrimispora', 'Alistipes_A', 'Anaerotruncus', 'Barnesiella', 'Micromonospora', 'Clavibacter', 'Bradyrhizobium', 'Angelakisella', 'Caecibacter', 'Enterococcus_A', 'Lactiplantibacillus', 'Dorea_A', 'Raoultibacter', 'Olsenella_B', 'Stomatobaculum', 'Lawsonibacter', 'Amedibacterium', 'Pseudoflavonifractor', 'Megasphaera', 'Bacillus_A', 'Enterococcus_D', 'Eubacterium', 'Turicibacter', 'Eubacterium_G', 'Sphingomonas', 'Mycobacterium', 'Veillonella', 'Bacteroides', 'Ligilactobacillus', 'Oribacterium', 'CAG-45', 'Janthinobacterium', 'Paenibacillus', 'Eubacterium_I', 'Erysipelatoclostridium', 'Lachnospira', 'Lactobacillus', 'Plantibacter', 'Weissella', 'An172', 'Carnobacterium', 'Clostridium_H', 'Sphingobium', 'Frisingicoccus', 'Blautia', 'Gemmiger', 'Rhodococcus_B', 'Arachnia', 'Aeriscardovia', 'Clostridium_AQ', 'Terrisporobacter', 'Coprobacillus', 'Oceanobacillus', 'Bacillus', 'Helicobacter_C', 'An181', 'Catonella', 'Phocea', 'Sellimonas', 'Dorea', 'UMGS966', 'Bacillus_H', 'Clostridium_P', 'Paraclostridium', 'Coprococcus', 'Limosilactobacillus', 'Eisenbergiella', 'Enterococcus', 'Ruminiclostridium', 'Lawsonella', 'Anaerostipes', 'Campylobacter']

# Assume you have already defined extracted_data

# Define the file path for the CSV file
csv_file = "filtered_median_range_L6.csv"

# Limit the taxon strings to only common strings
for entry in extracted_data:
    entry['taxon'] = entry['taxon'].split(';g__')[-1]

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