from documents.utils.xml_parser import parse_xml

def test_parse_xml_valid():
    sample = b'<root><item>Test</item></root>'
    assert '<item>Test</item>' in parse_xml(sample)

def test_parse_xml_invalid():
    invalid = b'<root><item>Test</root>'
    assert 'Invalid XML' in parse_xml(invalid)
