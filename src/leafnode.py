from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self,
                 tag: str | None,
                 value: str,
                 props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("leaf node must have a value")

        if not self.tag:
            return self.value

        rendered_html = f"<{self.tag}>{self.value}</{self.tag}>"
        if self.props:
            rendered_html = rendered_html\
                .replace(f"<{self.tag}>",
                         f"<{self.tag}{self.props_to_html()}>")

        return rendered_html
    

    def __repr__(self):
        return (
            f"LeafNode:\n"
            f"Tag: {self.tag}\n"
            f"Value: {self.value}\n"
            f"Props: {self.props_to_html()}"
        )

    