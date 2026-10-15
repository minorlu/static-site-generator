from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_block_type(markdown: str) -> BlockType:
    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    
    markdown_lines = markdown.split("\n")
    all_start_with_gt = True
    all_start_with_hyphen = True
    all_start_with_numbers = True

    # Quotes
    for line in markdown_lines:
        if not line.startswith(">"):
            all_start_with_gt = False
            break

    if all_start_with_gt:
        return BlockType.QUOTE

    # Unordered list
    for line in markdown_lines:
        if not line.startswith("- "):
            all_start_with_hyphen = False
            break

    if all_start_with_hyphen:
        return BlockType.UNORDERED_LIST

    # Ordered list
    for line_num in range(len(markdown_lines)):
        if not markdown_lines[line_num].startswith(f"{line_num + 1}. "):
            all_start_with_numbers = False
            break

    if all_start_with_numbers:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH