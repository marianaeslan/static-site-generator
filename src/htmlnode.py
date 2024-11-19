class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
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
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        