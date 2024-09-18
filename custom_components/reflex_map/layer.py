"""React-map-gl Layer Component."""

import reflex as rx 

class Layer(rx.Component):
    library = "react-map-gl"
    tag = "Layer"

    type: str = ""
    source: str = ""
    layout: dict = {"visibility": "none"}

    lib_dependencies: list[str] = ["react-map-gl"]   

def layer() -> rx.Component:
    return Layer.create()

layer = Layer.create