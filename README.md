# Static Site Generator

A Python-based static site generator project from [Boot.dev](https://boot.dev) that converts markdown files into HTML pages using templates. This project demonstrates file system operations, markdown processing, and HTML template handling.

## Features

* Recursively generates HTML pages from markdown files
* Maintains directory structure from content to public folder
* Supports markdown syntax including:
  * Headers
  * Lists
  * Bold/Italic text
  * Links
  * Code blocks
  * Blockquotes
* Template-based HTML generation

## Installation Requirements

* Python 3.x
* markdown2 library
  ```bash
  pip install markdown2

## Usage
1. Place your markdown files in the content directory
2. Ensure your template.html file is set up with a {{content}} placeholder
3. Run the generator:
```python main.py```
4. Find your generated HTML files in the public directory

## Learning Objectives
This project is part of the Boot.dev curriculum and focuses on:

- File system operations
- Recursive directory traversal
- Markdown to HTML conversion
- Template processing
- Basic web development concepts
