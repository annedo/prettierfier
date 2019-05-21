"""There's no way to write exactly what the expected result will be.

HTML/XML is impossible to actually parser with regex. 
Gotta manually check formatting of new lines is successful, regardless of whitespace."""


import re
from bs4 import BeautifulSoup
from pathlib import Path
import xml.dom.minidom as xmldom

from _context import prettierfier

from prettierfier import *

def test_prettify_xml():
    raw_xml = Path('xml/raw_xml.xml')

    Path('xml/test_default.xml').write_text(xmldom.parseString(raw_xml.read_text()).toprettyxml())
    Path('xml/test_default_opts.xml').write_text(xmldom.parseString(raw_xml.read_text()).toprettyxml(indent='', newl=''))
    
    Path('xml/test_xml.xml').write_text(prettify_xml(raw_xml.read_text()))

    soup = BeautifulSoup(raw_xml.read_text(), 'xml')
    Path('xml/bs4_xml_prettify.xml').write_text(prettify_xml(soup.prettify()))
    Path('xml/bs4_xml_encode.xml').write_text(prettify_xml(soup.encode().decode()))

def test_prettify_html(debug=False):
    text = Path('html/testhtml.html').read_text()
    parser = BeautifulSoup(text, 'html5lib')

    with open('html/rawprettify.html', 'w+') as file:
        file.write(parser.prettify())

    with open('html/rawtext.html', 'w+') as file:
        file.write(str(parser))

    with open('html/testprettify.html', 'w+') as file:
        file.write(prettify_html(parser.prettify(), debug))

    with open('html/testprettifytext.html', 'w+') as file:
        file.write(prettify_html(str(parser), debug))


test_prettify_xml()
test_prettify_html()