def markdown_to_blocks(markdown: str) -> list[str]:
    blocks_list = markdown.split("\n\n")
    strip_blocks_list = list(map(str.strip, blocks_list))

    return list(filter(None, strip_blocks_list))
