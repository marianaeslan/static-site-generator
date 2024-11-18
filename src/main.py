from textnode import TextNode, TextType

def main():
    # Test 1: Creating two identical nodes
    node1 = TextNode("Hello", TextType.TEXT, "https://test.com")
    node2 = TextNode("Hello", TextType.TEXT, "https://test.com")
    
    # Test 2: Creating a different node
    node3 = TextNode("Different", TextType.BOLD, "https://other.com")
    
    # Test __repr__
    print("Testing __repr__:")
    print(f"node1: {node1}")
    print(f"node2: {node2}")
    print(f"node3: {node3}")
    
    # Test __eq__
    print("\nTesting __eq__:")
    print(f"node1 == node2: {node1 == node2}")  # Should be True
    print(f"node1 == node3: {node1 == node3}")  # Should be False

if __name__ == "__main__":
    main()