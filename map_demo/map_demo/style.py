import reflex as rx

# Note: Using kebab-case for css properties in objects is not supported.

style = {
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
    "pre": {
        "maxWidth": "calc(100svw - 66px)",
        "overflowX": "auto"
    }
}