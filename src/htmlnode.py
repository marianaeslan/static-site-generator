class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError ("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        s = ""
        for k, v in self.props.items(): 
            s += f' {k}="{v}"'
        return s
    
    def __repr__(self):
        return f"HTMLNode(\ntag = {self.tag}, \nvalue = {self.value}, \nchildren = {self.children}, \nprops = {self.props}\n)"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props={}):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
class ParentNode(HTMLNode):
    def __init__(self,tag, children, props = {}):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if not self.tag:
            raise ValueError ("All Parent Nodes must have a tag")
        if not self.children:
            raise ValueError ("All Parent Nodes must have a children")

        children_html = "".join(child.to_html() for child in self.children)
        props_html = " ".join(f' {key}="{value}"' for key, value in self.props.items())
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"