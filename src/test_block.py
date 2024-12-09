import unittest
from block import *

class TestBlocks(unittest.TestCase):
    def setUp(self):
        self.text = "# Header\n\n\n\nParagraph\t\n\n* List" 
        self.res_text = markdown_to_blocks(self.text)

        self.mult_text = """
            # Heading 1

            This is a paragraph.

            * Item 1
            * Item 2
        """
        self.res_mult_text = markdown_to_blocks(self.mult_text)
        

    def test_mkd_to_blocks(self):
        self.assertListEqual(
            [
                '# Header',
                'Paragraph', 
                '* List',
            ],
            self.res_text,
        )
        self.assertListEqual(
            [
                "# Heading 1",
                "This is a paragraph.",
                "* Item 1\n* Item 2"
            ],
            self.res_mult_text,
        )
        
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_paragraph(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with *italic* text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
    - This is a list
    - with items
    - and *more* items

    1. This is an `ordered` list
    2. with items
    3. and more items

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
    # this is an h1

    this is paragraph text

    ## this is an h2
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
    > This is a
    > blockquote block

    this is paragraph text

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )   



if __name__ == "__main__":
    unittest.main()
