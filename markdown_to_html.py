import markdown_to_html


def open_file(filename: str) -> str:
    try:
        with open(filename, 'r') as file:
            return file.read()
    
    except IOError:
        print(f"Unable to open file: {filename}")
        return ""
    
def convert_to_html(markdown_text: str) -> str:
    return markdown_to_html.markdown_to_html(markdown_text)


file: str = input("Enter the markdown file name: ")
contents: str = open_file(file)
html: str = convert_to_html(contents)
print(f"The converted HTML code is: \n{html}")