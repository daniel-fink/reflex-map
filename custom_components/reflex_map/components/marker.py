"""https://visgl.github.io/react-map-gl/docs/api-reference/marker"""

from typing import Any
import reflex as rx 

class Marker(rx.Component):
    library = "react-map-gl"
    tag = "Marker"

    longitude: rx.Var[float]
    latitude: rx.Var[float]

    lib_dependencies: list[str] = ["react-map-gl"]


def marker() -> rx.Component:
    return Marker.create()

marker = Marker.create
