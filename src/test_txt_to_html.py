import unittest
from txt_to_html import text_node_to_html_node
from textnode import TextNode, TextType

class TestTxtHtml(unittest.TestCase):
    def setUp(self):
        self.node = TextNode("This is a raw text", TextType.TEXT)
        self.node2 = TextNode("This is a bold text", TextType.BOLD)
        self.node3 = TextNode("This is an italic text", TextType.ITALIC)
        self.node4 = TextNode("This is a code", TextType.CODE)
        self.node5 = TextNode("This is a link", TextType.LINK, "https://www.google.com")
        self.node6 = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev") 

    def test_text(self):
        html_node = text_node_to_html_node(self.node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a raw text")
        self.assertEqual(html_node.props, {}) 

    def test_bold(self):
        html_node = text_node_to_html_node(self.node2)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text")
        self.assertEqual(html_node.props, {}) 

    def test_text(self):
        html_node = text_node_to_html_node(self.node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a raw text")

    def test_italic(self):
        html_node = text_node_to_html_node(self.node3)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text") 
        self.assertEqual(html_node.props, {})   

    def test_img(self):
        html_node = text_node_to_html_node(self.node6)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")  
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "This is an image"}) 
    
    def test_raise_excep(self):
        self.node7 = TextNode("Invalid", "InvalidType")   
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(self.node7)
        self.assertEqual(str(context.exception), "TextNode invalid")




if __name__ == "__main__":
    unittest.main()