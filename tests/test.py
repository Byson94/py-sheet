f = open("/data/print.md")
print()

MARKDOWN = f.read()
from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)