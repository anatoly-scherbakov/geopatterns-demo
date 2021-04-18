import typer
from PIL import Image

from geopatterns_demo import draw
from geopatterns_demo.models import Method

app = typer.Typer()


@app.command()
def generate(text: str, method: Method = Method.XES):
    """Generate a geopattern image from command line."""
    png_content = draw.geopattern(text, method)
    image: Image.Image = Image.open(png_content)
    image.show()
