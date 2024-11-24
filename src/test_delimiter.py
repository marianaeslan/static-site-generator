import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter,extract_markdown_images, extract_markdown_links

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

if __name__ == "__main__":
    unittest.main()