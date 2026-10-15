import unittest
from blocktype import BlockType, block_to_block_type

class TestExtractMarkdown(unittest.TestCase):
    def test_threelevel_heading(self):
        md = "### as;l'fkl;l"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)
    def test_code(self):
        md = """```
asdjdfkl;jfsdaklafkjksld
```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)
    def test_quotes(self):
        md = """> asjdflkasdfjl;
> sjadl;fkjaslkdf
> fjdsklafjlkasdf"""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
    def test_ul(self):
        md = """- asjdflkasdfjl;
- sjadl;fkjaslkdf
- fjdsklafjlkasdf"""
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)
    def test_ol(self):
        md = """1. asjdflkasdfjl;
2. sjadl;fkjaslkdf
3. fjdsklafjlkasdf"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)
    def test_paragraph(self):
        md = "sfadfjhalksdfjlsdakfj"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()