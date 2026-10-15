import unittest
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text(self):
        splitted_nodes = split_nodes_delimiter(
            [TextNode("this is just text", TextType.TEXT)],
            "`",
            TextType.CODE
        )
        self.assertEqual(
            splitted_nodes,
            [TextNode("this is just text", TextType.TEXT)]
            )

    def test_delimiter_one_pair(self):
        splitted_nodes = split_nodes_delimiter(
            [TextNode("this is `code in` text", TextType.TEXT)],
            "`",
            TextType.CODE
        )
        self.assertEqual(
            splitted_nodes,
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("code in", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ]
        )

    def test_delimiter_two_pairs(self):
        splitted_nodes = split_nodes_delimiter(
            [TextNode("this is `code in` text and also `code`", TextType.TEXT)],
            "`",
            TextType.CODE
        )
        self.assertEqual(
            splitted_nodes,
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("code in", TextType.CODE),
                TextNode(" text and also ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ]
        )

    def test_beginning_delimiter(self):
        splitted_nodes = split_nodes_delimiter(
            [TextNode("`code in` text and also `code`", TextType.TEXT)],
            "`",
            TextType.CODE
        )
        self.assertEqual(
            splitted_nodes,
            [       
                TextNode("code in", TextType.CODE),
                TextNode(" text and also ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ]
        )

    def test_not_closed_delimiter(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter(
                [TextNode("`code in text and also `code`", TextType.TEXT)],
                "`",
                TextType.CODE
            )

    def test_only_bold(self):
        splitted_nodes = split_nodes_delimiter(
            [TextNode("**bold**", TextType.BOLD)],
            "**",
            TextType.BOLD
        )
        self.assertEqual(
            splitted_nodes, [TextNode("**bold**", TextType.BOLD)]
        )

    def test_few_nodes(self):
        splitted_nodes = split_nodes_delimiter(
            [
                TextNode("This is **bold** text", TextType.TEXT),
                TextNode("This is also **bold** text", TextType.TEXT)    
            ],
            "**",
            TextType.BOLD
        )
        self.assertEqual(
            splitted_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
                TextNode("This is also ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ]
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [test](google.com) "
            "and another [test2](youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("test", TextType.LINK, "google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("test2", TextType.LINK, "youtube.com"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()