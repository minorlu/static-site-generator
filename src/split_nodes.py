from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    splitted_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            splitted_nodes.append(old_node)
            continue
        
        md_images = extract_markdown_images(old_node.text)

        if len(md_images) == 0:
            splitted_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        for image_alt, image_link in md_images:
            sections = remaining_text.split(
                f"![{image_alt}]({image_link})", 1
                )
            if sections[0] != "":
                splitted_nodes.append(TextNode(
                    sections[0],
                    TextType.TEXT
                ))

            splitted_nodes.append(TextNode(
                image_alt,
                TextType.IMAGE,
                image_link
            ))

            remaining_text = sections[1]

        if remaining_text != "":
            splitted_nodes.append(TextNode(
                remaining_text,
                TextType.TEXT
            ))

    return splitted_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    splitted_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            splitted_nodes.append(old_node)
            continue
        
        md_links = extract_markdown_links(old_node.text)

        if len(md_links) == 0:
            splitted_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        for link_text, link_url in md_links:
            sections = remaining_text.split(
                f"[{link_text}]({link_url})", 1
                )
            if sections[0] != "":
                splitted_nodes.append(TextNode(
                    sections[0],
                    TextType.TEXT
                ))

            splitted_nodes.append(TextNode(
                link_text,
                TextType.LINK,
                link_url
            ))

            remaining_text = sections[1]

        if remaining_text != "":
            splitted_nodes.append(TextNode(
                remaining_text,
                TextType.TEXT
            ))

    return splitted_nodes