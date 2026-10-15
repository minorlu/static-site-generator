import unittest
from extract_markdown import extract_markdown_links, extract_markdown_images

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [text](google.com)"
        )
        self.assertListEqual([("text", "google.com")], matches)

if __name__ == "__main__":
    unittest.main()