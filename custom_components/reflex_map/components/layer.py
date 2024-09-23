"""https://maplibre.org/maplibre-style-spec/layers/"""

import reflex as rx 

class Layer(rx.Component):
    library = "react-map-gl"
    tag = "Layer"

    type: str = ""
    metadata: dict | None = None
    source: str | None = None
    # source-layer: str | None = None # need to figure out this piece for PMTiles
    minzoom: int | None = None
    maxzoom: int | None = None
    filter: list | None = None
    layout: dict | None = None
    paint: dict = {}

    lib_dependencies: list[str] = ["react-map-gl"]   

def layer() -> rx.Component:
    return Layer.create()

layer = Layer.create
