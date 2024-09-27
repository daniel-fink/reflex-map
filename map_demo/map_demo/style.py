import reflex as rx

# Note: Using kebab-case for css properties in objects is not supported.

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
        "fontSize": "1.25rem",
        "height": "70px",
        "lineHeight": "50px",
        "fontWeight": "bold",
        "backgroundColor": "#295DAA",
        "boxShadow": "0 2px 10px rgba(0, 0, 0, 0.1)",
        "padding": "10px 20px",
        "z-index": "200",
    },
    ".topNav a": {
        "color": "white",
        "textDecoration": "none",
        "lineHeight": "50px",
    },
    ".content": {
        "marginTop": "70px",
        "paddingTop": "20px",
        "marginBottom": "70px",
    },
    ".maplibregl-canvas-container": {
        "minHeight": "400px"
    },
    "canvas": {
        "height": "400px"
    },
    ".mapboxgl-control-container": {
        "position": "absolute",
        "bottom": "4px"
    },
}