import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "google.com")
        self.assertEqual(repr(node), 
                         "TextNode(This is a text node, bold, google.com)")

    def test_init(self):
        node = TextNode("This is a text node", TextType.BOLD, "google.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertEqual(node.url, "google.com")

    def test_different_text_types(self):
        node = TextNode("This is a text node", TextType.BOLD, "google.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "google.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def text_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")

    def test_link(self):
            node = TextNode("This is link text",
                            TextType.LINK,
                            "https://www.google.com/")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "a")
            self.assertEqual(html_node.value, "This is link text")
            self.assertEqual(html_node.props,
                             {"href": "https://www.google.com/"})

    def test_image(self):
                node = TextNode("This is image alt text",
                                TextType.IMAGE,
                                "https://www.google.com/")
                html_node = text_node_to_html_node(node)
                self.assertEqual(html_node.tag, "img")
                self.assertEqual(html_node.value, "")
                self.assertEqual(html_node.props,
                                 {"src": "https://www.google.com/",
                                  "alt": "This is image alt text"})

if __name__ == "__main__":
    unittest.main()