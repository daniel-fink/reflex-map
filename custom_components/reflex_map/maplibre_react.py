
# This will return the required React component.
# TODO: Any suggestions on how to improve this and handle all of this directly within Reflex would be greatly appreciated.
def get_maplibre_js():
    return """
    const extractFeatureFromEvent = (features) => {
        return features;
    };

    export const MapLibre = (props) => {
      const [map, setMap] = useState(null);

      const handleMouseClickEvent = (e, mouseEventFunction) => {
        if (!map) return;
        if (!e.point) return;
        const features = map.queryRenderedFeatures(e.point);
        return mouseEventFunction?.({ ...e, features });
      };

      useEffect(() => {
        const protocol = new pmtiles.Protocol();
        maplibregl.addProtocol("pmtiles", protocol.tile);
        return () => {
          maplibregl.removeProtocol("pmtiles");
        };
      }, []);

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