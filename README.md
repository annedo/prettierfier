# prettierfier
While I love [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), the BeautifulSoup.prettify() function adds a linebreak between *every* tag. 
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

This script parses HTML/XML as a raw string to more intelligently format tags.