"""React-map-gl Popup Component."""

import reflex as rx 

class Popup(rx.Component):
    library = "react-map-gl"
    tag = "Popup"
    
    latitude: float = 37.9677487
    longitude: float = -122.5727462

    anchor: str = "bottom"

    lib_dependencies: list[str] = ["react-map-gl"]   

class PopupState(rx.State):
    latitude: float = 37.9677487
    longitude: float = -122.5727462
    anchor: str = "bottom"

def popup() -> rx.Component:
    return Popup.create()

popup = Popup.create
