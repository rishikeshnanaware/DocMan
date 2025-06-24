import xml.etree.ElementTree as ET

def parse_xml(xml_bytes):
    try:
        root = ET.fromstring(xml_bytes)
        return ET.tostring(root, encoding='unicode')
    except ET.ParseError:
        return '<error>Invalid XML</error>'
