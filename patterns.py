"""List of Patterns to be Matched Against, providing a single location for all matches... Great for Troubleshooting"""

INLINE_LINK_PATTERN = r"(?<!\!)\[(?P<text>.+)\]\((?P<url>[^ )]+)( \"(?P<title>.+)\"){0,1}\)"
REFERENCE_PATTERN = r"(?<!\!)\[(?P<text>.+)\]\[(?P<reference>.+)\].+[?P=reference]: *(?P<url>.+)( \"(?P<title>.+)\"){0,1}\)$" # requires multiline