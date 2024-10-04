from utils import create_year_list

year_list = create_year_list(1990, 2023)
year_list = list(year_list)

car_tax_json = {
  "query": [
    {
      "code": "Sektori",
      "selection": {
        "filter": "item",
        "values": [
          "S1311"
        ]
      }
    },
    {
      "code": "Verolaji",
      "selection": {
        "filter": "item",
        "values": [
          "521001",
          "521002"
        ]
      }
    },
    {
      "code": "Vuosi",
      "selection": {
        "filter": "item",
        "values": [
          "1990",
          "1991",
          "1992",
          "1993",
          "1994",
          "1995",
          "1996",
          "1997",
          "1998",
          "1999",
          "2000",
          "2001",
          "2002",
          "2003",
          "2004",
          "2005",
          "2006",
          "2007",
          "2008",
          "2009",
          "2010",
          "2011",
          "2012",
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019",
          "2020",
          "2021",
          "2022",
          "2023"
        ]
      }
    },
    {
      "code": "Tiedot",
      "selection": {
        "filter": "item",
        "values": [
          "cp"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

newly_registered_cars_json = {
  "query": [
    {
      "code": "Ajoneuvoluokka",
      "selection": {
        "filter": "item",
        "values": [
          "01"
        ]
      }
    },
    {
      "code": "Käyttövoima",
      "selection": {
        "filter": "item",
        "values": [
          "01", # gasoline-cars
          "04" # e-cars
        ]
      }
    },
    {
      "code": "Vuosi",
      "selection": {
        "filter": "item",
        "values": year_list
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}
