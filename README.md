# prettierfier
While I love [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) as a parser, `BeautifulSoup.prettify()` adds a linebreak between *every* tag. 
This results in unwanted white space between tags that should be inline, like `<sup>`, `<a>`, `<span>`, etc:

```
<p>Introducing GitHub<sup>&reg;</sup></p>
```
<p>Introducing GitHub<sup>&reg;</sup></p>

vs.

```
<p>
    Introducing GitHub
    <sup>
        &reg;
    </sup>
</p>
```
<p>
    Introducing GitHub
    <sup>
        &reg;
    </sup>
</p>

This module parses HTML/XML as a raw string to more intelligently format tags.

## Installation

You have two options:
1. `pip install prettierfier` in your command line
2. Copy the contents of [prettierfier.py](prettierfier.py) to your own module.

This module is built with just the Python Standard Library and contains no external third-party dependencies.

## Functions

**prettify_xml**(*xml_string, indent=2, debug=False*)

* Can be used with no prior formatting.

```
    Args:
        xml_string (str): XML text to prettify.
        indent (int, optional): Set size of XML tag indents.

    Test-only args:
        debug (bool, optional): Show results of each regexp application.

    Returns:
        str: Prettified XML.
```

**prettify_html**(*html_string, debug=False*)

* Originally created to process `BeautifulSoup.prettify()` output.
* Does not add or remove regular line breaks. Can be used with regular HTML if it already has the newlines you want to keep.

```
    Args:
        html_string (str): HTML string to parse.

    Test-only args:
        debug (bool, optional): Show results of each regexp application.

    Returns:
        str: Prettified HTML.
```

## Example

```
import prettierfier

ugly_html = """<p>
    Introducing GitHub
    <sup>
        &reg;
    </sup>
</p>"""

pretty_html = prettierfier.prettify_html(ugly_html)
print(pretty_html) 

# Output
>>> <p>Introducing GitHub<sup>&reg;</sup></p>
```

### Links

* [GitHub](https://github.com/annedo/prettierfier)
* [PyPi](https://pypi.org/project/prettierfier/)