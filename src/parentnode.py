from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self,
                 tag: str,
                 children: list[HTMLNode],
                 props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("no tag")

        if not self.children:
            raise ValueError("no children")

        rendered_html = ""
        html_children = ""
        for child in self.children:
            html_children += child.to_html()
            rendered_html = f'<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>'

        return rendered_html