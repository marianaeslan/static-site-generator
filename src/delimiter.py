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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
        else:
            alt, url = images[0]
            sections = node.text.split(f"![{alt}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            if sections[1]:
                node_t = TextNode(sections[1], TextType.TEXT)
                t_nodes = split_nodes_image([node_t])
                new_nodes.extend(t_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
        else:
            anchor, link = links[0]
            sections = node.text.split(f"[{anchor}]({link})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor, TextType.LINK, link))
            if sections[1]:
                node_t = TextNode(sections[1], TextType.TEXT)
                t_nodes = split_nodes_link([node_t])
                new_nodes.extend(t_nodes)
    return new_nodes


def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    node = split_nodes_delimiter(node, "**", TextType.BOLD)
    node = split_nodes_delimiter(node, "*", TextType.ITALIC)
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    img = split_nodes_image(node)
    link = split_nodes_link(img)
    return link
    

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for block in blocks:
        block_lines = block.split("\n")
        cleaned_lines = [line.strip() for line in block_lines]
        cleaned_block = "\n".join(cleaned_lines)
        if cleaned_block:
            clean_blocks.append(cleaned_block.strip())
    
    return clean_blocks

