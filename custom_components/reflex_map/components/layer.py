"""https://maplibre.org/maplibre-style-spec/layers/"""

import reflex as rx 

class Layer(rx.Component):
    library = "react-map-gl"
    tag = "Layer"

    type: str = ""
    metadata: dict | None = None
    source: str | None = None
    minzoom: int | None = None
    maxzoom: int | None = None
    filter: list | None = None
    layout: dict | None = None
    source_layer: str | None = None
    paint: dict = {}

    lib_dependencies: list[str] = ["react-map-gl"]

    @classmethod
    def create(cls, *children, **props) -> 'Layer':
        layer_component = super().create(*children, **props)
        layer_component.custom_attrs.update({"source-layer": props.get("source_layer", "")})
        layer_component.custom_attrs.update({"ref": None})

        return layer_component


def layer() -> rx.Component:
    return Layer.create()

layer = Layer.create
