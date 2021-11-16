import pytest
from links import (
    parse_inline_link,
)

url_text = "foo"
url = "https://example.com"
url_title = "This is the title of the text"
reference_number = "1"
reference_name = "ref"
inline_link_test = f"[{url_text}]({url})"
inline_link_test_with_title = f'[{url_text}]({url} "{url_title}")'
inline_image_test = "![{url_text}]({url})"
reference_link_test = f"""[{url_text}][{reference_number}]
This text is ignored
[{reference_number}]: {url}"""
reference_link_text_is_refernce = f"""[{url_text}]
This text is ignored
[{url_text}]: {url}
"""

@pytest.mark.parametrize('text',
    [
        inline_image_test,
        reference_link_test
    ]
)
def test_inline_link_raises_on_image(text):
    with pytest.raises(ValueError) as e_info:
        parse_inline_link(text)


def test_inline_link_returns_text_and_url():
    match = parse_inline_link(inline_link_test)
    assert match['url'] == url
    assert match['text'] == url_text
    
 
def test_inline_link_returns_text_and_url():
    match = parse_inline_link(inline_link_test_with_title)
    assert match['url'] == url
    assert match['text'] == url_text
    assert match['title'] == url_title
  
  
  