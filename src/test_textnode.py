import unittest
from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
