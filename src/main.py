import os
import shutil

from markdown_to_html_node import markdown_to_html_node



def copy_static_to_public():
    public_dir = os.path.join(os.getcwd(), "public")
    shutil.rmtree(public_dir, ignore_errors=True)
    os.mkdir(public_dir)

    static_dir = os.path.join(os.getcwd(), "static")

    recursive_copy(static_dir, public_dir)


def recursive_copy(source, destination):
    source_dir_elements = os.listdir(source)

    for el in source_dir_elements:
        el_path = os.path.join(source, el)
        if os.path.isfile(el_path):
            shutil.copy(el_path, destination)
        else:
            os.mkdir(os.path.join(destination, el))
            recursive_copy(el_path, os.path.join(destination, el))


def extract_title(markdown):
    md_lines: list[str] = markdown.split("\n")
    title = ""
    for line in md_lines:
        if line.startswith("# "):
            title = line
            break

    if title == "":
        raise ValueError("there is no title in the markdown file")

    return title[2:].strip()

def generate_page(from_path, template_path, dest_path):
    from_path_full = os.path.join(os.getcwd(), from_path)
    template_path_full = os.path.join(os.getcwd(), template_path)
    dest_path_full = os.path.join(os.getcwd(), dest_path)

    print(f"Generating page from {from_path} "
    f"to {dest_path} using {template_path}")

    with open(from_path_full) as md_file:
        md_file_content = md_file.read()

    with open(template_path_full) as template_file:
        template_file_content = template_file.read()

    html_node = markdown_to_html_node(md_file_content)
    html_content = html_node.to_html()
    html_title = extract_title(md_file_content)

    template_file_content = template_file_content.replace(
        "{{ Title }}", html_title
        )
    template_file_content = template_file_content.replace(
        "{{ Content }}", html_content
        )

    os.makedirs(os.path.dirname(dest_path_full), exist_ok=True)

    with open(dest_path_full, 'w') as fp:
        fp.write(template_file_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dir_elements = os.listdir(dir_path_content)
    
    for el in content_dir_elements:
        el_path = os.path.join(dir_path_content, el)
        if os.path.isfile(el_path):
            dest_dir_path_full = os.path.join(
                dest_dir_path,
                el.replace(".md", ".html")
                )
            generate_page(el_path, template_path, dest_dir_path_full)
        else:
            os.mkdir(os.path.join(dest_dir_path, el))
            content_dir_path_full = os.path.join(dir_path_content, el)
            dest_dir_path_full = os.path.join(dest_dir_path, el)
            generate_pages_recursive(
                content_dir_path_full,
                template_path,
                dest_dir_path_full
            )


def main():
    copy_static_to_public()
    generate_pages_recursive(
        "content/",
        "template.html",
        "public/"
        )
    
main()