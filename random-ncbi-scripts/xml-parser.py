import xml.etree.ElementTree as ET
tree = ET.parse('biosample_result.xml')
root = tree.getroot()

for child in root:
    for x in child:
        if x.tag == "Ids":
            for y in x:
                if y.attrib.has_key('db'):
                    if y.attrib['db'] == "SRA":
                        print y.text
