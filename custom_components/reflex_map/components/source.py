"""https://maplibre.org/maplibre-style-spec/sources/"""

import reflex as rx 

class Source(rx.Component):
    library = "react-map-gl"
    tag = "Source"
    
    type: str = ""
    url: str | None = None
    tiles: list[str] | None = None
    data: str | dict| None = None
    bounds: list[float] | None = None
    scheme: str | None = None
    minzoom: int | None = None
    maxzoom: int | None = None
    attribution: str | None = None
    promoteId: str | None = None
    volatile: bool | None = None
    id: str = ""
    title: str | None = None
    tileSize: int | None = None
    
    lib_dependencies: list[str] = ["react-map-gl"]

    @classmethod
    def create(cls, *children, **props) -> 'Source':
        source_component = super().create(*children, **props)
        source_component.custom_attrs.update({"ref": None})

        return source_component


def source() -> rx.Component:
    return Source.create()

source = Source.create
