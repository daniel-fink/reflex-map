"""https://maplibre.org/maplibre-style-spec/layers/"""

import reflex as rx 

class Layer(rx.Component):
    library = "react-map-gl"
    tag = "Layer"

    type: str = ""
    metadata: rx.Var[dict | None]
    source: rx.Var[str | None]
    minzoom: rx.Var[int | None]
    maxzoom: rx.Var[int | None]
    filter: rx.Var[list | None]
    layout: rx.Var[dict | None]
    source_layer: rx.Var[str | None]
    paint: rx.Var[dict | None]

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
