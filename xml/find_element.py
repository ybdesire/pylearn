import xml.etree.ElementTree as ET
tree = ET.parse('1150.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

for neighbor in root.iter('object'):
    name = neighbor.find('name').text
    bndbox = neighbor.find('bndbox')
    xmin = bndbox.find('xmin').text
    ymin = bndbox.find('ymin').text
    xmax = bndbox.find('xmax').text
    ymax = bndbox.find('ymax').text
    print(name, xmin, ymin, xmax, ymax)

        
    