import unittest
from parser import *

class TestParser(unittest.TestCase):
	def test_splitNodesDelim_invalidSyntax(self):
		try:
			node = TextNode("This should **break", TextType.PLAIN)
			splitNodes = splitNodesDelim([node], "**", TextType.BOLD)
		except ValueError as e:
			self.assertEqual(e.__str__(), "Error: invalid Markdown syntax")

	def test_splitNodesDelim_bold(self):
		node = TextNode("This is text with a **bold** word", TextType.PLAIN)
		splitNodes = splitNodesDelim([node], "**", TextType.BOLD)
		self.assertEqual(
			splitNodes,
			[
				TextNode("This is text with a ", TextType.PLAIN),
				TextNode("bold", TextType.BOLD),
				TextNode(" word", TextType.PLAIN),
			]
		)
	
	def test_splitNodesDelim_italic(self):
		node = TextNode("This is text with an _italic_ word", TextType.PLAIN)
		splitNodes = splitNodesDelim([node], "_", TextType.ITALIC)
		self.assertEqual(
			splitNodes,
			[
				TextNode("This is text with an ", TextType.PLAIN),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word", TextType.PLAIN),
			]
		)
	
	def test_splitNodesDelim_code(self):
		node = TextNode("This is text with a `code block` word", TextType.PLAIN)
		splitNodes = splitNodesDelim([node], "`", TextType.CODE)
		self.assertEqual(
			splitNodes,
			[
				TextNode("This is text with a ", TextType.PLAIN),
				TextNode("code block", TextType.CODE),
				TextNode(" word", TextType.PLAIN),
			]
		)

	def test_splitNodesDelim_multipleItalic(self):
		node = TextNode("This is text with an _italic_ word. It also has _another_ italic word.", TextType.PLAIN)
		splitNodes = splitNodesDelim([node], "_", TextType.ITALIC)
		self.assertEqual(
			splitNodes,
			[
				TextNode("This is text with an ", TextType.PLAIN),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word. It also has ", TextType.PLAIN),
				TextNode("another", TextType.ITALIC),
				TextNode(" italic word.", TextType.PLAIN)
			]
		)
	
	def test_splitNodesDelim_notPlain(self):
		node = TextNode("This should do **nothing**", TextType.ITALIC)
		splitNodes = splitNodesDelim([node], "**", TextType.BOLD)
		self.assertEqual(splitNodes, [node])

	def test_splitNodesDelim_noDelim(self):
		node = TextNode("This should do nothing", TextType.PLAIN)
		splitNodes = splitNodesDelim([node], "**", TextType.BOLD)
		self.assertEqual(splitNodes, [node])
		splitNodes = splitNodesDelim([node], "_*", TextType.ITALIC)
		self.assertEqual(splitNodes, [node])
		splitNodes = splitNodesDelim([node], "`*", TextType.CODE)
		self.assertEqual(splitNodes, [node])