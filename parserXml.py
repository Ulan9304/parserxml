#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:14:02 2019

@author: rocket
"""
import os
import xml.etree.ElementTree as ET

def getBatchNameFromXML(XML_path):
    """
    <catalog>  главная ветка 
    
    <book id="bk101">
    <author>Gambardella, Matthew</author>
    <title>XML Developer's Guide</title>
    </book>
    
    <catalog/>
    """
    try:
        tree = ET.parse(XML_path)
        catalog = tree.getroot()
        batches = catalog.find("book") # тег который мы ищем в основной ветке
        batch = batches[0].attrib
        name = batch.get("author")
        return name
    
    except IOError as e:
        print (e)
        
path_to_program = "/home/rocket/parserxml"
data_directory = "/DATA"


path_to_XML = path_to_program + data_directory + "/XML/"
files_list = os.listdir(path_to_XML)

all_batch_Names = []
for file in files_list:
    all_batch_Names.append(getBatchNameFromXML(path_to_XML + file))
    
print(all_batch_Names)
print (getBatchNameFromXML(path_to_XML + file))
    