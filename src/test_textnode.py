import unittest
from textnode import TextNode, TextType, textNodeToHTMLNode


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
		self.assertEqual(node.url, None)
		node3 = TextNode("This is a text node", TextType.LINK, "https://leekspin.co")
		self.assertNotEqual(node, node3)
		self.assertNotEqual(node3.url, None)
		node4 = TextNode("I'M BACK BABY", TextType.LINK, "https://leekspin.co")
		self.assertNotEqual(node3, node4)
		node5 = TextNode("I'M BACK BABY", TextType.LINK, "https://meatspin.com")
		self.assertNotEqual(node4, node5)
	
	def test_text(self):
		node = TextNode("This is a plaintext node", TextType.PLAIN)
		html_node = textNodeToHTMLNode(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a plaintext node")

	def test_bold(self):
		node = TextNode("This is a bold node", TextType.BOLD)
		html_node = textNodeToHTMLNode(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is a bold node")
	
	def test_italic(self):
		node = TextNode("This is an italic node", TextType.ITALIC)
		html_node = textNodeToHTMLNode(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "This is an italic node")

	def test_code(self):
		node = TextNode("This is a code node", TextType.CODE)
		html_node = textNodeToHTMLNode(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "This is a code node")

	def test_link(self):
		node = TextNode("This is an anchor node", TextType.LINK, "https://leekspin.co")
		html_node = textNodeToHTMLNode(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "This is an anchor node")
		self.assertEqual(html_node.props_to_html(), " href=\"https://leekspin.co\"")

	def test_image(self):
		node = TextNode("This is an image node", TextType.IMAGE, "https://serenityforge.com/media/pages/games/needy-streamer-overload/6bc3c47648-1715702389/tall-hero.jpg")
		html_node = textNodeToHTMLNode(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props_to_html(), " src=\"https://serenityforge.com/media/pages/games/needy-streamer-overload/6bc3c47648-1715702389/tall-hero.jpg\" alt=\"This is an image node\"")


if __name__ == "__main__":
	unittest.main()
