import lxml 
from lxml import html
import requests
import pandas as pd 
import re
import bs4 

def find_cars(n, type=" "):

    """
    Tabulate top n cars by type.

    Parameters 
    ----------

    n : numeric value 

    b: "trucks" or "cheap"

    Returns: 
    -------

    pd.DataFrame


    Examples
    --------

    >>> import webscrape_carinfo
    >>> from webscrape_carinfo import find_cars 
    >>> n = 5
    >>> type = "trucks"
    >>> find_cars(5, type = "trucks")

                                     Model Name    Price Mileage
0                 2014 Ram 1500 Regular Cab  $19,990   70909
1                 2012 Ram 1500 Regular Cab  $20,990   44678
2             2016 Nissan Frontier Crew Cab  $24,990   65122
5                    2015 Ram 1500 Quad Cab  $27,590   73960
4  2015 Chevrolet Silverado 1500 Double Cab  $31,590   57645

    
    """

    import lxml 
    from lxml import html
    import requests
    if type == "cheap":
        cars_html =requests.get("https://www.carvana.com/cars/filters?cvnaid=eyJwcmljZSI6eyJtaW4iOjc5OTAsIm1heCI6MjAwMDB9fQ==")
        cars_doc = html.fromstring(cars_html.content)
        from bs4 import BeautifulSoup
        cars_content = cars_html.content
        soup = BeautifulSoup(cars_content, 'html.parser')
        carinfo = soup.find(class_='redesign__ResultsSection-sc-1gt0fs3-2 esqPNv')
        car_make = [a.text for a in carinfo.find_all(class_="make-model")]
        price = [a.text for a in carinfo.find_all(class_="flex flex-col h-full justify-end")]
        mileage = [a.text for a in carinfo.find_all(class_="trim-mileage")]
        import re
        regex = r"[!\"#\$%&\'\(\)\*\+,-\./:;<=>\?@\[\\\]\^_`{\|}~]"
        subst = ""
        result = re.sub(regex, subst, str(mileage), 0, re.MULTILINE)
        mileage_d = re.findall(r'\d{4,8}', result)
        miles = list(map(str, mileage_d))
        import pandas as pd 
        df = pd.DataFrame({'Model Name': car_make, 'Price':price, 'Mileage': miles, 'Engine Type': mileage})
        df=df.sort_values(by='Price', ascending=True)
        print(df.head(n))

    if type =="trucks":

        trucks_html =requests.get("https://www.carvana.com/cars/truck")
        trucks_doc = html.fromstring(trucks_html.content)
        from bs4 import BeautifulSoup
        trucks_content = trucks_html.content
        soup = BeautifulSoup(trucks_content, 'html.parser')
        trucksinfo = soup.find(class_='redesign__ResultsSection-sc-1gt0fs3-2 esqPNv')
        car_make = [a.text for a in trucksinfo.find_all(class_="make-model")]
        price = [a.text for a in trucksinfo.find_all(class_="flex flex-col h-full justify-end")]
        mileage = [a.text for a in trucksinfo.find_all(class_="trim-mileage")]
        import re
        regex = r"[!\"#\$%&\'\(\)\*\+,-\./:;<=>\?@\[\\\]\^_`{\|}~]"
        subst = ""
        result = re.sub(regex, subst, str(mileage), 0, re.MULTILINE)
        mileage_d = re.findall(r'\d{4,8}', result)
        miles = list(map(str, mileage_d))
        import pandas as pd 
        df = pd.DataFrame({'Model Name': car_make, 'Price':price, 'Mileage': miles})
        df=df.sort_values(by='Price', ascending=True)
        print(df.head(n))

    else: 
        return print("Please enter either type = 'cheap' or type = 'trucks', and a numeric value for n. Otherwise, please check website mannually: https://www.carvana.com ")