from display_data import app

def test_001_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#header', timeout=8)

def test_002_graph(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#sales-graph', timeout=8)

def test_003_region(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#region', timeout=8)