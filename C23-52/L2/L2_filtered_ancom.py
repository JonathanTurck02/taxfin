#C23-52, L2 filtered ancom
#4/4/24

import csv

ANCOMBC_dict = {}

#this is going to need to be different for this proect
with open("/Users/jonathanturck/Documents/C23-52_v2/taxfin_inputs/L2_phylum.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        taxon = row[0]
        pvalue1 = float(row[20]) #comparison 0.2AA_Day-7 v 0.2AA_Day30
        qvalue1 = float(row[26]) # 0.2AA_Day30
        pvalue2 = float(row[21]) # 0.2AA_Day7
        qvalue2 = float(row[27]) # 0.2AA_Day7
        pvalue3 = float(row[22]) # 6ODHA_Day-7
        qvalue3 = float(row[28]) # 6ODHA_Day-7
        pvalue4 = float(row[23]) # 6ODHA_Day30
        qvalue4 = float(row[29]) # 6ODHA_Day30
        pvalue5 = float(row[24]) # 6ODHA_Day7
        qvalue5 = float(row[30]) # 6ODHA_Day7

        ANCOMBC_dict[taxon] = {'p_0.2AA_day30': pvalue1, 'q_0.2AA_day30': qvalue1, 'p_0.2AA_day7': pvalue2, 
                               'q_0.2AA_day7': qvalue2, 'p_60ODHA_day-7': pvalue3, 'q_6ODHA_day-7': qvalue3,
                               'p_6ODHA_day30': pvalue4, 'q_6ODHA_day30': qvalue4, 'p_6ODHA_day7': pvalue5,
                                'q_6ODHA_day7': qvalue5}
new_ANCOMBC_dict = {}

# Iterate over the keys of the ANCOMBC_dict and remove 'p__' from each key
for taxon, values in ANCOMBC_dict.items():
    # Remove 'p__' from the taxon entry and strip any leading or trailing spaces
    new_taxon = taxon.replace('p__', '').strip()
    # Add the entry with the modified taxon name to the new dictionary
    new_ANCOMBC_dict[new_taxon] = values

print(new_ANCOMBC_dict)

common_taxons = ['Firmicutes', 'Bacteroidetes', 'Fusobacteria', 'Other', 'Proteobacteria', 'Deferribacteres', 'Actinobacteria']

filtered_data_dict = {}

for taxon, values in new_ANCOMBC_dict.items():
    if taxon in common_taxons:
        filtered_data_dict[taxon] = values

with open('C23-52/L2/L2_filtered_ANCOMBC.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['taxon', 'p_0.2AA_day30', 'q_0.2AA_day30','p_0.2AA_day7','q_0.2AA_day7','q_6ODHA_day-7','p_6ODHA_day30','q_6ODHA_day30','p_6ODHA_day7','q_6ODHA_day7'])
    # Write the data rows
    for taxon, values in filtered_data_dict.items():
        csvwriter.writerow([taxon, values['p_0.2AA_day30'], values['q_0.2AA_day30'],
                                        values['p_0.2AA_day7'], values['q_0.2AA_day7'],
                                        values['p_60ODHA_day-7'], values['q_6ODHA_day-7'],
                                        values['p_6ODHA_day30'], values['q_6ODHA_day30'],
                                        values['p_6ODHA_day7'], values ['q_6ODHA_day7']])
print(f"Successfully wrote L3_filtered_ancom.csv")