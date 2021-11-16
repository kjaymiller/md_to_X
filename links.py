import re
import patterns

def parse_inline_link(md_text: str) -> dict:
    """given the markdown sequence [foo](http://example.com)create a groupdicts with text='foo' and url='http://example.com'.
    
    NOTE: This will not validate the url itself.
    """

    matcher = re.compile(patterns.INLINE_LINK_PATTERN)
    match = matcher.match(md_text)
    
    if not match:
       raise ValueError(f"{md_text=} does not match inline link pattern")
       
    return  match.groupdict()
    
    
def parse_reference_link(md_text: str) -> dict:
    """given the markdown pattern:
        [foo][1]
        [1]: https://example.com.
    create a groupdicts with text='foo' and url='http://example.com'.
        
    NOTE: This will not validate the url itself.
    """
    
    matcher = re.compile(patterns.REFERENCE_LINK_PATTERN, re.M)
    match = matcher.match(md_text)
    
    if not match:
       raise ValueError(f"{md_text=} does not match inline link patter")
       
    return  match.groupdict()