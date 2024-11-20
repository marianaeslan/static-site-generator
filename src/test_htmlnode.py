import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
        

class TestParentNode(unittest.TestCase):
    def setUp(self):
        """Child Nodes"""
        self.child_node = LeafNode("p", "Hi, there!")
        self.child_node2 = LeafNode("a", "click here", {"href":"https://www.bootdev.com"})
        self.child_node3 = LeafNode("h1", "This is a Title")
        self.child_node4 = LeafNode("b", "Bold Text")
        self.child_node5 = LeafNode("i", "Italic Text")
        self.child_node6 = LeafNode(None, "Normal Text")

        """Parent Nodes"""
        self.node = ParentNode("a", [self.child_node2, self.child_node3], {"href":"https://www.google.com"})
        self.node2 = ParentNode("div", [self.child_node, self.child_node2],{"class": "image-wrap"})
        self.node3 = ParentNode("div", None,{"class": "image-wrap"}) # no children
        self.node4 = ParentNode(None,[self.child_node, self.child_node2]) # no tag
        self.node5 = ParentNode("p", [self.child_node4, self.child_node6, self.child_node5])
        self.inner_node = ParentNode("p", [self.child_node4, self.child_node6])
        self.outer_node = ParentNode("div", [LeafNode(None, "Outer Text"), self.inner_node])

    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            self.node3.to_html()
        self.assertEqual(str(context.exception), "All Parent Nodes must have a children")

    def test_no_tag(self):
        with self.assertRaises(ValueError) as context:
            self.node4.to_html()
        self.assertEqual(str(context.exception), "All Parent Nodes must have a tag")
    
    def test_to_html(self):
        self.assertEqual(self.node5.to_html(), "<p><b>Bold Text</b>Normal Text<i>Italic Text</i></p>")
        self.assertEqual(self.node2.to_html(), '<div class="image-wrap"><p>Hi, there!</p><a href="https://www.bootdev.com">click here</a></div>')
        self.assertEqual(self.outer_node.to_html(), "<div>Outer Text<p><b>Bold Text</b>Normal Text</p></div>")



if __name__ == "__main__":
    unittest.main()