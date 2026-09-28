"""Shared visual branding constants for the NYC mobility notebooks."""

BRAND_COLORS = {
    "dark_teal": "#006D77",
    "seafoam": "#83C5BE",
    "ice": "#EDF6F9",
    "pale_peach": "#FFDDD2",
    "terracotta": "#E29578",
}

# Core ordered sequence for simple branded charts.
BRAND_COLOR_SEQUENCE = [
    BRAND_COLORS["dark_teal"],
    BRAND_COLORS["terracotta"],
    BRAND_COLORS["seafoam"],
    BRAND_COLORS["pale_peach"],
    BRAND_COLORS["ice"],
]

# Diverging sequence for signed comparisons.
BRAND_DIVERGING_SEQUENCE = [
    BRAND_COLORS["dark_teal"],
    BRAND_COLORS["seafoam"],
    BRAND_COLORS["ice"],
    BRAND_COLORS["pale_peach"],
    BRAND_COLORS["terracotta"],
]

# Sequential heatmap scale for 0-to-1 concentration views.
BRAND_SEQUENTIAL_HEATMAP_SCALE = [
    [0.00, "#FFFFFF"],
    [0.20, BRAND_COLORS["ice"]],
    [0.45, BRAND_COLORS["seafoam"]],
    [0.70, "#5FB8B1"],
    [1.00, BRAND_COLORS["dark_teal"]],
]

# Map-oriented semantic roles.
BRAND_MAP_COLORS = {
    "primary": BRAND_COLORS["dark_teal"],
    "secondary": BRAND_COLORS["terracotta"],
    "supporting": BRAND_COLORS["seafoam"],
    "background": BRAND_COLORS["ice"],
    "soft_highlight": BRAND_COLORS["pale_peach"],
    "outline": "#7FAEB5",
}

# Geometry styling defaults for branded choropleths.
BRAND_MAP_STYLE = {
    "marker_line_color": "#7FAEB5",
    "marker_line_width": 0.5,
    "marker_opacity": 0.7,
}

# Categorical palette for cluster maps and other discrete geography views.
BRAND_CLUSTER_PALETTE = [
    "#006D77",
    "#E29578",
    "#83C5BE",
    "#B56576",
    "#5E8F96",
    "#F0B7A4",
    "#CDB4DB",
]

BRAND_PLOTLY_TEMPLATE = {
    "layout": {
        "paper_bgcolor": "white",
        "plot_bgcolor": BRAND_COLORS["ice"],
        "font": {"color": BRAND_COLORS["dark_teal"]},
        "colorway": BRAND_COLOR_SEQUENCE,
    }
}

def apply_branding(fig):
    """Apply the shared NYC mobility Plotly layout defaults to an existing figure.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        Plotly figure to style.

    Returns
    -------
    plotly.graph_objects.Figure
        The same figure after applying shared paper/background, font, and
        color-sequence defaults. Existing figure-specific titles, axes,
        dimensions, margins, and other layout settings are preserved unless
        they conflict with these shared defaults.
    """
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor=BRAND_COLORS["ice"],
        font={"color": BRAND_COLORS["dark_teal"]},
        colorway=BRAND_COLOR_SEQUENCE,
    )
    return fig