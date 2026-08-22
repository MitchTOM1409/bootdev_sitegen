from textnode import *

def splitNodesDelim(oldNodes: list[TextNode], delim: str, textType: TextType) -> list[TextNode]:
	newNodes: list[TextNode] = []
	for oldNode in oldNodes:
		if oldNode.textType != TextType.PLAIN:
			newNodes.append(oldNode)
			continue
		splitText = oldNode.text.split(delim)
		if len(splitText) % 2 == 0:
			raise ValueError("Error: invalid Markdown syntax")
		
		newNodes.extend(
			[
				TextNode(splitText[i], TextType.PLAIN if i % 2 == 0 else textType) for i in range(len(splitText))
			]
		)
	return newNodes