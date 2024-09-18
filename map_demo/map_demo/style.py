import reflex as rx

style = {
    ".wrapper": {
        "overflow": "auto",
    },
    ".sidebar": {
        "position": "fixed",
        "right": "0",
        "top": "0",
        "width": "250px",
        "height": "calc(100vh - 40px)",
        "background-color": "#f4f4f4",
        "box-shadow": "-2px 0 10px rgba(0, 0, 0, 0.1)",
        "padding": "20px",
        "z-index": "100",
        "margin-top": "40px",
        "overflow": "auto",
    },
    ".topNav": {
        "color": "white",
        "position": "fixed",
        "top": "0",
        "left": "0",
        "width": "100%",
        "height": "40px",
        "line-height": "20px",
        "background-color": "#000e35",
        "box-shadow": "0 2px 10px rgba(0, 0, 0, 0.1)",
        "padding": "10px 20px",
        "z-index": "200",
    },
    ".content": {
        "margin-top": "40px",
        "margin-right": "250px",
        "background-color": "#f9f9f9",
        "min-height": "calc(100vh - 40px)",
    },
    ".maplibregl-canvas-container": {
        "height": "calc(100vh - 40px) !important"
    },
    "canvas": {
        "height": "calc(100vh - 40px) !important"
    },
    ".mapboxgl-control-container": {
        "position": "absolute",
        "bottom": "4px"
    }
}
