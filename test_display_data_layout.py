import dash
from dash import html
from selenium.webdriver.common.by import By

def test_001_header(dash_br):
    dash_br.server_url = "http://127.0.0.1:8050"
    dash_br.driver.find_elements(By.ID, "header")

def test_002_graph(dash_br):
    dash_br.server_url = "http://127.0.0.1:8050"
    dash_br.driver.find_elements(By.ID, "sales-graph")

def test_003_region(dash_br):
    dash_br.server_url = "http://127.0.0.1:8050"
    dash_br.driver.find_elements(By.ID, "region")