import xml.etree.ElementTree as ET
tree = ET.parse('xx.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)


