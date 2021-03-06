import folium

from stravaviz.get_strava_data import get_activity_polylines


def create_map(center, style):
    """Creates base folium map.

    Args:
        center (list): Coordinates [lat, long] for center of map.
        style (str): Style of map - either 'dark' or 'light'.

    Returns:
        folium.Map: Base map.
    """
    tile_styles = {
        'dark': 'Cartodb dark_matter',
        'light': 'Cartodb positron'
    }

    strava_map = folium.Map(
        location=center,
        tiles=tile_styles[style],
        zoom_start=13
    )

    return strava_map


def add_polyline(folium_map, polyline, color='deepskyblue'):
    """Adds polyline to base map.

    Args:
        folium_map (folium.Map): Map to add polyline to.
        polyline (str): Decoded polyline string.
        color (str): Optional, color of polyline.

    Returns:
        folium.Map: Map with polyline added on.
    """

    polyline = folium.PolyLine(
        locations=polyline,
        weight=0.5,
        opacity=0.4,
        color=color
    ).add_to(folium_map)

    return folium_map


def create_heatmap(center, style='dark', color='deepskyblue', activities={}):
    """Creates heatmap with activity polylines.

    Args:
        center (list): Coordinates [lat, long] for center of map.
        style (str): Optional, style of map. Either 'dark' or 'light'.
        color (str): Optional, color of activity polylines.
        activities (dict): Optional parameters for retrieved
            activities. Format below. Default retrieves all activities.
            {
                'after': 'YYYY-MM-DD',
                'before': 'YYYY-MM-DD',
                'limit': int
            }

    Returns:
        folium.Map: Heatmap with polylines.
    """
    strava_map = create_map(center, style)
    polylines = get_activity_polylines(**activities)
    for polyline in polylines:
        add_polyline(strava_map, polyline, color)

    return strava_map
