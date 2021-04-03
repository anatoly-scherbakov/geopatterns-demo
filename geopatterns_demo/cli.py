import typer

from geopatterns_demo import draw
from geopatterns_demo.models import Method

app = typer.Typer()


@app.command()
def generate(text: str, method: Method = Method.XES):
    print(draw.geopattern(text, method))
