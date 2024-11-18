import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.node = TextNode("This is a text node", TextType.BOLD, None)
        self.node2 = TextNode("This is a text node", TextType.BOLD, None)

    def test_eq(self):
        """Test the __eq__ function"""
        self.assertEqual(self.node, self.node2)
    
    def test_urlisNone(self):
        """Check if the url is really None"""
        self.assertIsNone(self.node.url)
    
    def test_urlEqual(self):
        """Check if the URL are the same"""
        self.node.url = "www.test.com"
        self.node2.url = "www.test.com"
        self.assertEqual(self.node, self.node2)
    
    def test_textType(self):
        """Check if the text type is different from each other"""
        self.node.text_type = TextType.ITALIC
        self.assertNotEqual(self.node, self.node2)

    def test_text(self):
        """Check if the text is different from each other"""
        self.node2.text = "This is a test"
        self.assertNotEqual(self.node, self.node2)
    
    def test_repr(self):
        self.node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(self.node)
        )
    


if __name__ == "__main__":
    unittest.main()