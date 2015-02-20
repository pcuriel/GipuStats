__author__ = 'josubg'


import urllib2
import xml.etree.ElementTree as ET
import pandas.io.parsers

response = urllib2.urlopen('http://api.gipuzkoairekia.eus/dataset/buscar?texto=catastro&numRes=100000000')
html = response.read()


tree = ET.fromstring(html)
files = []
for dataset in tree.findall("datasets/dataset"):
    titulo = dataset.find("titulo").text
    titulo = titulo[titulo.index('(')+1:-1].title()
    for recurso in dataset.findall("documentosAsociados/recurso/url"):
        csv_text = urllib2.urlopen(recurso.text)
        csv_text.skip
        dataFrame = pandas.io.parsers.read_fwf(
            csv_text,
            [(0, 2), (4, 11), (13, 19), (21, 21), (23, 25), (27, 29), (31, 34), (36, 65), (67, 70),
             (72, 73), (75, 76), (78, 80), (82, 83), (85, 93), (95, 96)])
        files.append((titulo, csv_text, dataFrame))

print dataFrame[1]
for f in files:

dataFrame()

print "recursos encontrados: " + str(len(files))

    #csv_text = urllib2.urlopen(a.text).read()
