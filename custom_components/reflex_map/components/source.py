"""https://maplibre.org/maplibre-style-spec/sources/"""

import reflex as rx 

class Source(rx.Component):
    library = "react-map-gl"
    tag = "Source"
    
    type: rx.Var[str | None] = ""
    url: rx.Var[str | None] = None
    tiles: list[str] | None = None
    data: rx.Var[str | dict | None] = None
    bounds: rx.Var[list[float] | None] = None
    scheme: rx.Var[str | None] = None
    minzoom: rx.Var[int | None] = None
    maxzoom: rx.Var[int | None] = None
    attribution: rx.Var[str | None] = None
    promoteId: rx.Var[str | None] = None
    volatile: rx.Var[bool | None] = None
    title: rx.Var[str | None] = None
    tileSize: rx.Var[int | None] = None
    
    
    lib_dependencies: list[str] = ["react-map-gl"]

    @classmethod
    def create(cls, *children, **props) -> 'Source':
        source_component = super().create(*children, **props)
        source_component.custom_attrs.update({"ref": None})

        return source_component


def source() -> rx.Component:
    return Source.create()

source = Source.create
