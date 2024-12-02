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



if __name__ == "__main__":
    unittest.main()
