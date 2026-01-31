import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
from dash import dcc, html


def find_component(component, component_type, component_id=None):
    """
    Recursively search Dash layout for a component type (and optional id)
    """
    if isinstance(component, component_type):
        if component_id is None or getattr(component, "id", None) == component_id:
            return True

    if hasattr(component, "children"):
        children = component.children
        if isinstance(children, list):
            for child in children:
                if find_component(child, component_type, component_id):
                    return True
        else:
            return find_component(children, component_type, component_id)

    return False


def test_header_is_present():
    layout = app.layout
    assert find_component(layout, html.H1)


def test_graph_is_present():
    layout = app.layout
    assert find_component(layout, dcc.Graph, "sales-line-chart")


def test_region_picker_is_present():
    layout = app.layout
    assert find_component(layout, dcc.RadioItems, "region-radio")
