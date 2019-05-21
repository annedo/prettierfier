"""There's no way to write exactly what the expected result will be.

HTML/XML is impossible to actually parser with regex.
Must Manually check formatting of new lines is successful, regardless of
existing whitespace.
"""

from bs4 import BeautifulSoup
from pathlib import Path
import xml.dom.minidom as xmldom

from _context import prettierfier
from prettierfier import *


def test_prettify_xml():
    raw_xml = Path('xml/_raw_xml.xml')

    Path('xml/test_default.xml').write_text(
        xmldom.parseString(raw_xml.read_text()).toprettyxml()
        )

    Path('xml/test_default_opts.xml').write_text(
        xmldom.parseString(raw_xml.read_text()).toprettyxml(indent='', newl='')
        )

    Path('xml/test_xml.xml').write_text(prettify_xml(raw_xml.read_text()))

    soup = BeautifulSoup(raw_xml.read_text(), 'xml')
    Path('xml/bs4_xml_prettify.xml').write_text(prettify_xml(soup.prettify()))
    Path('xml/bs4_xml_encode.xml').write_text(
        prettify_xml(soup.encode().decode()))


def test_prettify_html(debug=False):
    text = Path('html/_raw_html.html').read_text()
    parser = BeautifulSoup(text, 'html5lib')

    Path('html/html_default_prettify.html').write_text(parser.prettify())

    Path('html/html_default_text.html').write_text(str(parser))

    Path('html/html_test_bs4prettify.html').write_text(
        prettify_html(parser.prettify(), debug))

    Path('html/html_test_prettifytext.html').write_text(
        prettify_html(str(parser), debug))


def test_prettify_html_min(debug=False):
    text = Path('html/_raw_html_min.html').read_text()
    parser = BeautifulSoup(text, 'html5lib')

    Path('html/min_default_prettify.html').write_text(parser.prettify())

    Path('html/min_default_text.html').write_text(str(parser))

    Path('html/min_test_bs4prettify.html').write_text(
        prettify_html(parser.prettify(), debug))

    Path('html/min_test_prettifytext.html').write_text(
        prettify_html(str(parser), debug))


test_prettify_xml()
test_prettify_html()
test_prettify_html_min()
