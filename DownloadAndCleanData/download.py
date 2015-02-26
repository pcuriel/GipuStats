__author__ = 'josubg'


import urllib2
import xml.etree.ElementTree as ET
import pandas.io.parsers

response = urllib2.urlopen('http://api.gipuzkoairekia.eus/dataset/buscar?texto=catastro&numRes=100000000')
html = response.read()

tree = ET.fromstring(html)
i = 0
for dataset in tree.findall("datasets/dataset"):
    title = dataset.find("titulo").text
    title = title[title.index('(')+1:-1].title()
    for resource in dataset.findall("recursos/recurso"):
        tipo = ""
        if resource.find("nombreFichero").text.startswith("ficherourbanaparcelamunicipio"):
            tipo = "Parcelas"
        else:
            tipo = "Locales"
        
        resource_url = resource.find("url").text
        print "Downloading", resource_url
        f = urllib2.urlopen(resource_url)
        csv = open("data/raw/" + title.replace("/", "-") + "_" + tipo + ".csv", "wb")
        csv.write(f.read())
        csv.close()
        i += 1

print "Downloaded", i, "files"
