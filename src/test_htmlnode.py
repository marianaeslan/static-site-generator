import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node= HTMLNode("a", "click here", None, {"href":"https://www.google.com"})
        self.node2 = HTMLNode("div", "Hello, world!", None, None)
        self.node3 = HTMLNode("img", None, None, {"src": "image.jpg", "alt": "A sample image"})

    def test_no_props(self):
        self.assertEqual(self.node2.props_to_html(), "")

    def test_props(self):
        self.assertEqual(self.node.props_to_html(),' href="https://www.google.com" ')
    
    def test_mult_props(self):
        self.assertEqual(self.node3.props_to_html(),' src="image.jpg"  alt="A sample image" ')

    def test_repr(self):
        self.assertEqual(self.node.__repr__(), "HTMLNode(\ntag = a, \nvalue = click here, \nchildren = None, \nprops = {'href': 'https://www.google.com'}\n)")

    def test_to_html_err(self):
        with self.assertRaises(NotImplementedError):
            HTMLNode.to_html(self)

if __name__ == "__main__":
    unittest.main()