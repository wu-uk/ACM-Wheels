import pyperclip

def create_snippet():
    name = input("name:\n")
    prefix = input("prefix:\n")
    description = input("description:\n")
    print("code: (Ctrl+Z then Enter to finish)")
    
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    
    snippet = f'"{name}": {{\n' \
              f'    "prefix": "{prefix}",\n' \
              f'    "description": "{description}",\n' \
              f'    "body": [\n'
    
    for i, line in enumerate(lines):
        snippet += f'        "{line}"'
        if i < len(lines) - 1:
            snippet += ','
        snippet += '\n'
    
    snippet += '    ]\n}'
    
    pyperclip.copy(snippet)
    print("\nSnippet copied to clipboard!")

if __name__ == "__main__":
    create_snippet()