#!/usr/bin/env python3

"""Parse and display car information from an XML file.

This script reads an XML file ('cars.xml') containing a list of cars for sale,
parses it using the ElementTree XML parser, and prints the structure of each car
entry, including tags, attributes, and text values. The XML is expected to have a
root element 'cars_for_sale' containing 'car' element, each with child elements
such as 'id', 'brand', 'model', 'production_year', and 'price' (with a 'currency'
attribute).

Dependencies:
    - xml.etree.ElementTree: Standard library module for XML parsing.
    - cars.xml: An XML file in the same directory, structured and described.

Example Output:
    cars_for_sale
        car
            id = 1
            brand = Ford
            model = Mustag
            production_year = 1972
            price {'currency': 'USD'} = 35900
        car
            id = 2
            brand = Aston Martin
            model = Rapide
            production_year = 2010
            price {'currency': 'GBP'} = 32000
"""

import xml.etree.ElementTree as ET

cars_for_sale = ET.parse('cars.xml').getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
        print(' =', prop.text)
