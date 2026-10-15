from htmlnode import HTMLNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown: str) -> HTMLNode:
    md_blocks: list[str] = markdown_to_blocks(markdown)
    html_nodes = []

    for block in md_blocks:
        block_type = block_to_block_type(block)
        html_node = create_html_node_by_blocktype(block, block_type)
        html_nodes.append(html_node)

    return ParentNode("div", html_nodes)    



def create_html_node_by_blocktype(block: str, block_type: BlockType) -> HTMLNode:
    match block_type:
        case BlockType.QUOTE:
            block_lines = block.split("\n")
            block_text = ""
            for line in block_lines:
                block_text += line.removeprefix(">").removeprefix(" ") + "\n"

            block_children = text_to_children(block_text.rstrip("\n"))

            return ParentNode("blockquote", block_children)
        
        case BlockType.PARAGRAPH:
            return ParentNode("p", text_to_children(block.replace("\n", " ")))
        
        case BlockType.HEADING:
            i = 0
            while block[i] != " ":
                i += 1
            return ParentNode(f"h{i}", text_to_children(block.split(" ", 1)[1]))

        case BlockType.CODE:
            strip_block = block.removeprefix("```\n").removesuffix("```")
            leaf_node = text_node_to_html_node(TextNode(
                strip_block, TextType.CODE)
                )
            return ParentNode("pre", [leaf_node])

        case BlockType.UNORDERED_LIST:
            block_lines = block.split("\n")
            block_children = []
            for line in block_lines:
                item_text = line.removeprefix("-").removeprefix(" ")
                block_children.append(ParentNode(
                    "li", text_to_children(item_text))
                    )

            return ParentNode("ul", block_children)

        case BlockType.ORDERED_LIST:
            block_lines = block.split("\n")
            block_children = []
            for line in block_lines:
                item_text = line.split(" ", 1)[1]
                block_children.append(ParentNode(
                    "li", text_to_children(item_text))
                    )

            return ParentNode("ol", block_children)



def text_to_children(text: str) -> list[HTMLNode]:
    children = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        children.append(text_node_to_html_node(node))

    return children