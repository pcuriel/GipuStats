__author__ = 'pcuriel'


import pandas
import sys
from os import listdir

def load_locales_df(town_name):
    locales = None
    locales = pandas.io.parsers.read_fwf(
        open("data/raw/" + town_name + "_Locales.csv", 'r'),
             [(0, 3), (4, 11), (12, 19), (20, 21), (22, 25), (26, 29), (30, 34), (35, 65), (66, 70),
              (71, 73), (74, 76), (77, 80), (81, 83), (84, 93), (94, 96)],
             header=None, skiprows=3)
    # Load the file to get the column names
    f = open("data/raw/" +  town_name + "_Locales.csv", 'r')
    #  Skip the first two columns (separator string and column names in basque)
    f.readline()
    f.readline()
    locales.columns = f.readline().rstrip("\n").split(",")
    f.close()
    
    return locales

def load_parcelas_df(town_name):
    return pandas.io.parsers.read_csv(open("data/raw/" + town_name + "_Parcelas.csv", 'r'), header=0, skiprows=2)
    
# Get the town names
town_names = [i[:-12] for i in listdir("data/raw") if i.endswith("_Locales.csv")]

# Load the Locales and Parcelas of the first town
locales = load_locales_df(town_names[0])
parcelas = load_parcelas_df(town_names[0])
town_codes = [parcelas["MUNICIPIO"][0]]

# And process the rest of the towns
for town in town_names[1:]:
    print "Processing", town
    # Some towns have no data for the Locales CSV. That's why both functions are try-catched separatedly.
    try:
        local = load_locales_df(town)
        locales = pandas.concat([locales, local])
    except:
        print "Unexpected error with Locales:", sys.exc_info()[0]
    
    try:
        parcela = load_parcelas_df(town)
        parcelas = pandas.concat([parcelas, parcela])
        town_codes.append(parcela["MUNICIPIO"][0])
    except:
        print "Unexpected error with Parcelas:", sys.exc_info()[0]

print "Saving CSVs..."
locales.to_csv("data/Locales.csv", index=False)
parcelas.to_csv("data/Parcelas.csv", index=False)
town_codes_df = pandas.DataFrame({"CODIGO" : town_codes, "NOMBRE": town_names})
town_codes_df.to_csv("data/Municipios.csv", index=False)
