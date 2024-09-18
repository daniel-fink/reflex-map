
# This will return the required React component.
# It handles all of the maplibre-gl imports and dependencies as well as some adds controls.
# TODO: Any suggestions on how to improve this and handle all of this directly within Reflex would be greatly appreciated.
def get_maplibre_js():
    return """
    const extractFeatureFromEvent = (features) => {
        return features;
    };

    import Map from "react-map-gl";
    import maplibregl from "maplibre-gl";
    import "maplibre-gl/dist/maplibre-gl.css";
    import "@stadiamaps/maplibre-search-box/dist/style.css";
    import "@watergis/maplibre-gl-legend/dist/maplibre-gl-legend.css";
    import * as pmtiles from "pmtiles";
    import { MapLibreSearchControl } from "@stadiamaps/maplibre-search-box";
    import { MaplibreLegendControl } from "@watergis/maplibre-gl-legend";

    export const MapLibre = (props) => {
      const [map, setMap] = useState(null);

      // We need to handle these controls dynamically as well.
      // Whether that's injecting custom code or finding a way to handle this within Reflex.
      // At the moment it looks like injecting custom code is the way to go but we just need to find a way to make it easier.
      useEffect(() => {
        if (!map) return;
        const fullScreenControl = new maplibregl.FullscreenControl();
        const navControl = new maplibregl.NavigationControl();

        const searchControl = new MapLibreSearchControl({
          useMapFocusPoint: true,
        });

        // Still need a way to handle the legend, need to be able to dynamically generate
        // this based on the Reflex configuration.
        const legendControl = new MaplibreLegendControl(
          { google_maps: "Google Maps" },
          {
            title: "Legend",
            onlyRendered: false,
          }
        );
        map.addControl(fullScreenControl);
        map.addControl(navControl);
        map.addControl(searchControl, "top-left");
        map.addControl(legendControl, "top-left");

        return () => {
          map.removeControl(fullScreenControl);
          map.removeControl(searchControl);
          map.removeControl(navControl);
          map.removeControl(legendControl);
        };
      }, [map]);

      useEffect(() => {
        const protocol = new pmtiles.Protocol();
        maplibregl.addProtocol("pmtiles", protocol.tile);
        return () => {
          maplibregl.removeProtocol("pmtiles");
        };
      }, []);

      const handleMouseClickEvent = (e, mouseEventFunction) => {
        if (!map) return;
        if (!e.point) return;
        const features = map.queryRenderedFeatures(e.point);
        return mouseEventFunction?.({ ...e, features });
      };

      return (
        <Map
          ref={setMap}
          mapLib={maplibregl}
          {...props}
          onMouseDown={(e) => handleMouseClickEvent(e, props.onMouseDown)}
          onMouseUp={(e) => handleMouseClickEvent(e, props.onMouseUp)}
          onMouseMove={(e) => handleMouseClickEvent(e, props.onMouseMove)}
          onClick={(e) => handleMouseClickEvent(e, props.onClick)}
        />
      );
    };
    """
