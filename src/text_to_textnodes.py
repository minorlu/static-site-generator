from textnode import TextNode, TextType
from split_nodes import split_nodes_link, split_nodes_image
from split_nodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    text_nodes = split_nodes_delimiter(
        [TextNode(text, TextType.TEXT)], "`", TextType.CODE
    )
    text_nodes = split_nodes_delimiter(
        text_nodes, "**", TextType.BOLD
    )
    text_nodes = split_nodes_delimiter(
        text_nodes, "_", TextType.ITALIC
    )

    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)

    return text_nodes