from enum import Enum
from htmlnodes.leafnode import LeafNode

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

def textNodeToHTMLNode(textNode: TextNode) -> LeafNode:
	match textNode.textType:
		case TextType.PLAIN:
			return LeafNode(None, textNode.text)
		case TextType.BOLD:
			return LeafNode("b", textNode.text)
		case TextType.ITALIC:
			return LeafNode("i", textNode.text)
		case TextType.CODE:
			return LeafNode("code", textNode.text)
		case TextType.LINK:
			return LeafNode("a", textNode.text, {"href": textNode.url})
		case TextType.IMAGE:
			return LeafNode("img", "", {"src": textNode.url, "alt": textNode.text})
		case _:
			raise ValueError("Error: Invalid text node type")