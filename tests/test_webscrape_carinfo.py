from webscrape_carinfo import webscrape_carinfo
import pandas as pd 
import lxml 
from lxml import html
import requests
import re
import bs4 


def test_find_cars():
    expected = None 
    actual= webscrape_carinfo.find_cars(5, type= "sedan")
    assert actual == expected
