import re


def extract_markdown_images(text):
    regex_pattern = r"!\[(.*?)\]\((.*?)\)"
    images = re.findall(regex_pattern, text)

    return images

def extract_markdown_links(text):
    regex_pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    links = re.findall(regex_pattern, text)

    return links