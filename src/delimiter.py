import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        parts = node.text.split(delimiter)

        if len(parts)% 2 == 0:
           raise ValueError ("Invalid markdown")
        
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        
        new_nodes.extend(split_nodes)
    return new_nodes
            
def extract_markdown_images(text):
    """Regex pattern that captures alt text and images"""
    img_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    img = re.findall(img_pattern, text)
    return img


def extract_markdown_links(text):
    """Regex pattern that captures links and anchor text"""
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    link = re.findall(link_pattern, text)
    return link
            

    

            

