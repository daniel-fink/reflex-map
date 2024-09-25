import reflex as rx

style = {
    ".wrapper": {
        "overflow": "auto",
    },
    ".sidebar": {
        "width": "250px",
    },
    ".topNav": {
        "color": "white",
        "position": "fixed",
        "top": "0",
        "left": "0",
        "width": "100%",
        "font-size": "1.25rem",
        "height": "70px",
        "line-height": "50px",
        "font-weight": "bold",
        "background-color": "#295DAA",
        "box-shadow": "0 2px 10px rgba(0, 0, 0, 0.1)",
        "padding": "10px 20px",
        "z-index": "200",
    },
    ".topNav a": {
        "color": "white",
        "text-decoration": "none",
        "line-height": "50px",
    },
    ".content": {
        "margin-top": "70px",
        "padding-top": "20px",
        "margin-bottom": "70px",
    },
    ".maplibregl-canvas-container": {
        "min-height": "400px"
    },
    "canvas": {
        "height": "400px"
    },
    ".mapboxgl-control-container": {
        "position": "absolute",
        "bottom": "4px"
    },
}