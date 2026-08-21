from htmlnodes.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == "":
            raise ValueError("Error: Parent nodes must have a tag")
        if len(self.children) == 0:
            return ValueError("Error: Parent nodes must have children")
        return f"<{self.tag}{self.props_to_html()}>{"".join([child.to_html() for child in self.children])}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props_to_html()})"