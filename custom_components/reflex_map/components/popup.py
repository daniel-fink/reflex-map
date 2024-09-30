"""React-map-gl Popup Component."""

import reflex as rx 

class Popup(rx.Component):
    library = "react-map-gl"
    tag = "Popup"
    
    latitude: rx.Var[float]
    longitude: rx.Var[float]
    anchor: str = "bottom"

    lib_dependencies: list[str] = ["react-map-gl"]   

def popup() -> rx.Component:
    return Popup.create()

popup = Popup.create
