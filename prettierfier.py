import re
import xml.dom.minidom as xmldom
import xml.etree.ElementTree as xmlTree

def apply_tag_re(string, instructions_obj):
    processed_string = instructions_obj['regex'].sub(instructions_obj['sub'], string)
    return processed_string

def apply_re_subs(string, instructions_obj_list, debug=False):
    processed_string = string
    for instructions_obj in instructions_obj_list:
        processed_string = instructions_obj['regex'].sub(instructions_obj['sub'], processed_string)
        if debug:
            print('============================================================================\n')
            print(instructions_obj['regex'])
            print('----------------------------------------------------------------------------\n')
            print(processed_string)
    return processed_string

def prettify_xml(xml_string, indent=2, debug=False):
    doc = xmldom.parseString(xml_string)
    indent_str = ' ' * indent
    uglyXml = doc.toprettyxml(indent=indent_str)
    
    inline_all_tags = {
        'regex': re.compile(r'>\n\s*([^<>\s].*?)\n\s*</', re.DOTALL),
        'sub': r'>\g<1></'
    }
    
    whitespace_re = {
        'regex': re.compile(r'^[\s\n]*$', re.MULTILINE),
        'sub': ''
    }
    
    empty_tags = {
        'regex': re.compile(r'(<[^/]*?>)(\n|\s)*(</)', re.MULTILINE),
        'sub': r'\g<1>\g<3>'
    }

    blankline_re = {
        'regex': re.compile(r'(>)\n$', re.MULTILINE),
        'sub': r'\g<1>'
    }

    regexps = [inline_all_tags, whitespace_re, empty_tags, blankline_re]
    pretty_xml = apply_re_subs(uglyXml, regexps, debug)
    return pretty_xml

    #text_re = re.compile(r'>[\n\s]*([^<>\s].*?)[\n\s]*</', re.DOTALL)
    #prettyXml = text_re.sub(r'>\g<1></', uglyXml)
#
    #blankline_re = re.compile(r'^[\s\n]*$', re.MULTILINE)
    #newline_re = re.compile(r'^\n', re.MULTILINE)
    #prettierXml = blankline_re.sub('', prettyXml)
    #prettierXml = newline_re.sub('', prettierXml)
#
    #return prettierXml
#
def prettify_html(html_string, debug=False):
    """Correct inline HTML tags being split with newlines by default BeautifulSoup.prettify() method."""

    inline_all_tags = {
        'regex': re.compile(r'>\n\s+([^<>\s].*?)\n\s*</', re.DOTALL),
        'sub': r'>\g<1></'
    }

    # I like having an actual newline after a <br> tag. The space is for keeping words seperate on minification.
    br = {
        'regex': re.compile(r'\n\s*(<br.*?>)', re.DOTALL),
        'sub': r'\g<1> '
    }

    # Superscripts are always attached to the ends of words.
    sup_start = {
        'regex': re.compile(r'[\n\s]*(<(sup|wbr).*?>)[\n\s]*', re.DOTALL|re.M),
        'sub': r'\g<1>'
    }

    # Superscripts are separated from following words with a space.
    sup_end_space = {
        'regex': re.compile(r'[\n\s]*(</sup>)([a-zA-Z0-9])', re.DOTALL),
        'sub': r'\g<1> \g<2>'
    }

    # Removes white space between superscript and immediately following tag
    sup_end_tag = {
        'regex': re.compile(r'[\n\s]*(</sup>)[\n\s]*(<)', re.DOTALL),
        'sub': r'\g<1> \g<2>'
    }

    # Inlining common inline elements
    strong_a_start = {
        'regex': re.compile(r'[\n\s]*(<(strong|a|span).*?>)[\n\s]*', re.DOTALL),
        'sub': r' \g<1>'
    }

    # Removes whitespace between end of these inline tags and begining of new tag
    strong_a_end = {
        'regex': re.compile(r'[\n\s]*(</(strong|a|span)>)[\n\s]*(<)', re.DOTALL),
        'sub': r'\g<1>\g<3>'
    }

    # Adds a space between the ending inline tags and following words
    strong_a_endspace = {
        'regex': re.compile(r'[\n\s]*(</(strong|a|span)>)([a-zA-Z0-9])', re.DOTALL),
        'sub': r'\g<1> \g<3>'
    }

    # Removes spaces between nested inline tags
    nested_spaces_start = {
        'regex': re.compile(r'(<[^/]*?>) (?=<)'),
        'sub': r'\g<1>'
    }

    # Removes spaces between nested end tags -- which wont have attributes so can be differentiated by string only content
    nested_spaces_end = {
        'regex': re.compile(r'(</\w*?>) (?=</)'),
        'sub': r'\g<1>'
    }

    # Adds breaks between open/close <html> tags and removes newline before </body> tag if str(parser) is used instead of parser.prettify()
    html_tag_start = {
        'regex': re.compile(r'(<html>)(?=<)'),
        'sub': r'\g<1>\n '
    }

    html_tag_end = {
        'regex': re.compile(r'(</body>)(</html>)'),
        'sub': r' \g<1>\n\g<2>'
    }

    end_body_newline = {
        'regex': re.compile(r'\n\s+(\n\s*(?=</body>))'),
        'sub': r'\g<1>'
    }

    # Make empty tags inline
    empty_tags = {
        'regex': re.compile(r'(<(?P<tag_name>.*?)>)[\n\s]+(</(?P=tag_name))'),
        'sub': r'\g<1>\g<3>'
    }

    regexps = [inline_all_tags, br, sup_start, sup_end_tag, sup_end_space, strong_a_start, strong_a_end, strong_a_endspace, nested_spaces_start, nested_spaces_end, html_tag_start, html_tag_end, end_body_newline, empty_tags] 
    pretty_html = apply_re_subs(html_string, regexps, debug)
    return pretty_html