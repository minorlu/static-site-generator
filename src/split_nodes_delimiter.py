from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode],
                          delimiter: str,
                          text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        splitted_text = old_node.text.split(delimiter)

        if len(splitted_text) % 2 == 0:
            raise Exception("invalid Markdown syntax")

        for text_part_index in range(len(splitted_text)):
            if splitted_text[text_part_index] == "":
                continue

            if text_part_index % 2 == 0:
                new_nodes.append(TextNode(
                    splitted_text[text_part_index],
                    TextType.TEXT
                ))
            else:
                new_nodes.append(TextNode(
                    splitted_text[text_part_index],
                    text_type
                ))

    return new_nodes