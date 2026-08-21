class HTMLNode:
    def __init__(self, 
                 tag: str | None = None,
                 value: str| None = None,
                 children: list["HTMLNode"] | None = None, 
                 props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props.copy() if props is not None else None

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        return (' ' + ' '.join([f"{k}=\"{v}\"" for k, v in self.props.items()])) if self.props is not None else ""

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, [{", ".join(self.children)}], {self.props_to_html()}"
