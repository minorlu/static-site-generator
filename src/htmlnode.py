class HTMLNode:
    def __init__(self,
                 tag: str | None = None,
                 value: str | None = None,
                 children: HTMLNode | None = None,
                 props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        html_props = ""
        for key, value in self.props.items():
            html_props += f' {key}="{value}"'

        return html_props

    def __repr__(self):
        return (
            f"HTMLNode:\n"
            f"Tag: {self.tag}\n"
            f"Value: {self.value}\n"
            f"Children: [{self.children}]\n"
            f"Props: {self.props_to_html()}"
        )