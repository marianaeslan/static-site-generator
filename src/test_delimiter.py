import unittest
from textnode import TextNode, TextType
from delimiter import *

class TestDelimiter(unittest.TestCase):
    def setUp(self):
        self.bold_node = TextNode("This text have a **bold** word", TextType.TEXT)
        self.new_bold_node = split_nodes_delimiter([self.bold_node], "**", TextType.BOLD)

        self.italic_node = TextNode("This text have an *italic* word", TextType.TEXT)
        self.new_italic_node = split_nodes_delimiter([self.italic_node], "*", TextType.ITALIC)

        self.double_bold_node = TextNode("This text have one **bold** word and **another**", TextType.TEXT)
        self.new_double_node = split_nodes_delimiter([self.double_bold_node], "**", TextType.BOLD)

        self.mult_styles_node = TextNode("**Bold** and *Italic*", TextType.TEXT)
        self.new_mult_node = split_nodes_delimiter([self.mult_styles_node],"**", TextType.BOLD)
        self.new_mult_node = split_nodes_delimiter(self.new_mult_node, "*", TextType.ITALIC)

        self.code_node = TextNode("This is a text with a `code block` word", TextType.TEXT)
        self.new_code_node = split_nodes_delimiter([self.code_node], "`", TextType.CODE)

    def test_bold_delimiter(self):
        self.assertListEqual(
            [
                TextNode("This text have a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            self.new_bold_node,
        )
    
    def test_italic_delimiter(self):
        self.assertListEqual(
            [
                TextNode("This text have an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            self.new_italic_node,
        )
    
    def test_double_bold(self):
        self.assertListEqual(
            [
                TextNode("This text have one ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            self.new_double_node,
        )
    
    def test_multiple_styles(self):
        self.assertListEqual(
            [
                TextNode("Bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("Italic", TextType.ITALIC),
            ],
            self.new_mult_node,
        )
    
    def test_code_block(self):
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            self.new_code_node,
        )

class TestExtractor(unittest.TestCase):
    def setUp(self):
        self.text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.text_match = extract_markdown_images(self.text)

        self.text_2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.text_match_2 = extract_markdown_links(self.text_2)

    def test_altText_links(self):
        self.assertEqual(self.text_match, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_anchor_url(self):
        self.assertEqual(self.text_match_2, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

class TestSplit(unittest.TestCase):
    def setUp(self):
        self.node_link = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        self.new_nodes_link = split_nodes_link([self.node_link])

        self.node_img = TextNode(
            "This is text with an image ![example](https://example.com/image.png) and more text.",
            TextType.TEXT
        )
        self.new_nodes_img = split_nodes_image([self.node_img])

        self.node_mult_img = TextNode(
            "Here is ![image1](https://example.com/image1.png) and ![image2](https://example.com/image2.png)",
            TextType.TEXT
        )
        self.nodes_mult_imgs = split_nodes_image([self.node_mult_img])
        
        self.node_mult_link = TextNode(
            "Check [Google](https://www.google.com) and [GitHub](https://github.com)",
            TextType.TEXT
        )
        self.nodes_mult_links = split_nodes_link([self.node_mult_link])
        

    def test_splitLinks(self):
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            self.new_nodes_link,
        )

        self.assertListEqual(
            [
                TextNode("Check ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("GitHub", TextType.LINK, "https://github.com"),
            ],
            self.nodes_mult_links
        )
    
    def test_splitImages(self):
        self.assertListEqual(
            [
                TextNode("This is text with an image ", TextType.TEXT),
                TextNode("example", TextType.IMAGE, "https://example.com/image.png"),
                TextNode(" and more text.", TextType.TEXT),
            ],
            self.new_nodes_img
        )

        self.assertListEqual(
            [
                TextNode("Here is ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "https://example.com/image1.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "https://example.com/image2.png"),
            ],
            self.nodes_mult_imgs
        )

class TestTxtNodes(unittest.TestCase):
    def setUp(self):
        self.node_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.node_list = text_to_textnodes(self.node_text)

    def test_text_to_textNodes(self):
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            self.node_list,
        )



if __name__ == "__main__":
    unittest.main()