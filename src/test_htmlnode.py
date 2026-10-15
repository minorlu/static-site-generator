import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        html_node = HTMLNode()
        self.assertRaises(NotImplementedError, html_node.to_html)

    def test_props_to_html(self):
        html_node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(html_node.props_to_html(),
                         ' href="https://www.google.com"')

    def test_repr(self):
        children_node = HTMLNode(value="i'm children")
        html_node = HTMLNode("p", "test value",
                             children_node,
                             {"href": "https://www.google.com"})
        expected = (
        "HTMLNode:\n"
        "Tag: p\n"
        "Value: test value\n"
        "Children: [HTMLNode:\n"
        "Tag: None\n"
        "Value: i'm children\n"
        "Children: [None]\n"
        "Props: ]\n"
        'Props:  href="https://www.google.com"'
        )

        self.assertEqual(repr(html_node), expected)   


if __name__ == "__main__":
    unittest.main()