import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        self.assertEqual(
            text_to_textnodes("just plain text"),
            [TextNode("just plain text", TextType.TEXT)],
        )

    def test_bold(self):
        self.assertEqual(
            text_to_textnodes("before **bold** after"),
            [
                TextNode("before ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" after", TextType.TEXT),
            ],
        )

    def test_italic(self):
        self.assertEqual(
            text_to_textnodes("before _italic_ after"),
            [
                TextNode("before ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" after", TextType.TEXT),
            ],
        )

    def test_code(self):
        self.assertEqual(
            text_to_textnodes("before `code` after"),
            [
                TextNode("before ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" after", TextType.TEXT),
            ],
        )

    def test_image(self):
        self.assertEqual(
            text_to_textnodes("before ![cat](https://example.com/cat.png) after"),
            [
                TextNode("before ", TextType.TEXT),
                TextNode("cat", TextType.IMAGE, "https://example.com/cat.png"),
                TextNode(" after", TextType.TEXT),
            ],
        )

    def test_link(self):
        self.assertEqual(
            text_to_textnodes("before [site](https://example.com) after"),
            [
                TextNode("before ", TextType.TEXT),
                TextNode("site", TextType.LINK, "https://example.com"),
                TextNode(" after", TextType.TEXT),
            ],
        )

    def test_all_types(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image",
                    TextType.IMAGE,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_markdown_inside_code(self):
        text = (
            "`**bold** _italic_ "
            "![image](https://example.com/image.png) "
            "[link](https://example.com)`"
        )

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode(
                    "**bold** _italic_ "
                    "![image](https://example.com/image.png) "
                    "[link](https://example.com)",
                    TextType.CODE,
                ),
            ],
        )


if __name__ == "__main__":
    unittest.main()