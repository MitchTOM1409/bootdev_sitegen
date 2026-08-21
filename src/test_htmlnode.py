import unittest
from htmlnodes.htmlnode import HTMLNode
from htmlnodes.leafnode import LeafNode
from htmlnodes.parentnode import ParentNode

class TestHTMLNode(unittest.TestCase):
	def test_props_to_html(self):
		prop_dict = {
			"href": "https://leekspin.co"
		}
		node = HTMLNode(props = prop_dict)
		self.assertEqual(node.props_to_html(), " href=\"https://leekspin.co\"")
		prop_dict["href"] = "https://www.google.com"
		prop_dict["target"] = "_blank"
		node2 = HTMLNode(props = prop_dict)
		self.assertEqual(node2.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
		
		self.assertNotEqual(node.props_to_html(), node2.props_to_html())
	
	def test_leaf_to_html_p(self):
		try:
			node = LeafNode("p", "Hello, world!")
			self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
			node2 = LeafNode("p", "fuck ice")
			self.assertNotEqual(node.to_html(), node2.to_html())
			LeafNode("p", "").to_html()
		except ValueError as e:
			self.assertEqual(e.__str__(), "Error: Non-image leaf nodes must have a value")
	
	def test_leaf_to_html_notag(self):
		node = LeafNode(None, "Hello, world!")
		self.assertEqual(node.to_html(), "Hello, world!")
		node2 = LeafNode(None, "fuck ice")
		self.assertNotEqual(node.to_html(), node2.to_html())

	def test_leaf_to_html_a(self):
		prop_dict = {
			"href": "https://leekspin.co"
		}
		node = LeafNode("a", "Click on me!", prop_dict)
		self.assertEqual(node.to_html(), "<a href=\"https://leekspin.co\">Click on me!</a>")
		prop_dict["href"] = "https://www.google.com"
		prop_dict["target"] = "_blank"
		node2 = LeafNode("a", "this brick looks real throwable", prop_dict)
		self.assertNotEqual(node.to_html(), node2.to_html())

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)
	
	def test_to_html_with_no_tag(self):
		try:
			ParentNode("", [LeafNode("span", "child")])
		except ValueError as e:
			self.assertEqual(e.__str__(), "Error: Parent nodes must have a tag")

	def test_to_html_with_no_children(self):
		try:
			ParentNode("div", [])
		except ValueError as e:
			self.assertEqual(e.__str__(), "Error: Parent nodes must have children")
	
	def test_to_html_with_multiple_children(self):
		children = [
			LeafNode("b", "child 1"),
			LeafNode(None, "child 2")
		]
		parent = ParentNode("div", children)
		self.assertEqual(
			parent.to_html(),
			"<div><b>child 1</b>child 2</div>"
		)


if __name__ == "__main__":
	unittest.main()
