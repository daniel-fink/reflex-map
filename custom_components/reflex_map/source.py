"""React-map-gl Source Component."""

import reflex as rx 

class Source(rx.Component):
    library = "react-map-gl"
    tag = "Source"
    
    type: str = ""
    title: str = ""
    tileSize: int = 256
    tiles: list[str] = []

    lib_dependencies: list[str] = ["react-map-gl"]


def source() -> rx.Component:
    return Source.create()

source = Source.create