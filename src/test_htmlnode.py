import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node = HTMLNode("a", "click here", None, {"href":"https://www.google.com"})
        self.node2 = HTMLNode("div", "Hello, world!", None, None)
        self.node3 = HTMLNode("img", None, None, {"src": "image.jpg", "alt": "A sample image"})

    def test_no_props(self):
        self.assertEqual(self.node2.props_to_html(), "")

    def test_props(self):
        self.assertEqual(self.node.props_to_html(),' href="https://www.google.com"')
    
    def test_mult_props(self):
        self.assertEqual(self.node3.props_to_html(),' src="image.jpg" alt="A sample image"')

    def test_repr(self):
        self.assertEqual(self.node.__repr__(), "HTMLNode(\ntag = a, \nvalue = click here, \nchildren = None, \nprops = {'href': 'https://www.google.com'}\n)")

    
class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.node = LeafNode("a", "click here", {"href":"https://www.google.com"})
        self.node2 = LeafNode("div", "Hello, world!", None)
        self.node3 = LeafNode("img", None, {"src": "image.jpg", "alt": "A sample image"})
        self.node4 = LeafNode("p", "Hello, world!")
    
    def test_to_html_no_value(self):
        with self.assertRaises(ValueError) as context:
            self.node3.to_html()
        self.assertEqual(str(context.exception), "All leaf nodes must have a value")

    def test_to_html_no_tag(self):
        self.node3.tag = None
        self.node3.value = "Insert text here" 
        self.assertEqual(self.node3.to_html(), "Insert text here")

    def test_to_html_no_children(self):
        self.assertEqual(self.node4.to_html(), "<p>Hello, world!</p>")

    def test_to_html(self):
        self.assertEqual(self.node2.to_html(), '<div>Hello, world!</div>')
        

if __name__ == "__main__":
    unittest.main()