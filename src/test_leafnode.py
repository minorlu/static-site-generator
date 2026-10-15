import unittest
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),
                         '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(repr(node),
                         "LeafNode:\n"
                         "Tag: p\n"
                         "Value: Hello, world!\n"
                         "Props: ")

if __name__ == "__main__":
    unittest.main()