from enum import Enum

class TextType(Enum):
    PLAIN = "plaintext"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, textType: TextType, url: str | None = None):
        self.text: str = text
        self.textType: textType = textType
        self.url: str | None = url

    def __eq__(self, other):
        return self.text == other.text and self.textType == other.textType and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.textType.value}, {self.url})"
