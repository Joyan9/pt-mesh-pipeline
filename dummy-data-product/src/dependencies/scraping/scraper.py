import requests

def getFloridaPT():
    url = "https://scoc.fdot.gov/api/ActiveContract/GetContracts"

    payload = ""
    headers = {
        "cookie": "ARRAffinity=35978001fd73e046abf1a291514067177a6ad8707b422922a48343fc5cc1c4f6; ARRAffinitySameSite=35978001fd73e046abf1a291514067177a6ad8707b422922a48343fc5cc1c4f6",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9,en-GB;q=0.8,en-IN;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "nmstat=4b02e659-eb77-098b-dc6f-64a497f27f91; ARRAffinity=35978001fd73e046abf1a291514067177a6ad8707b422922a48343fc5cc1c4f6; ARRAffinitySameSite=35978001fd73e046abf1a291514067177a6ad8707b422922a48343fc5cc1c4f6",
        "Expires": "Sat, 01 Jan 2020 00:00:00 GMT",
        "Pragma": "no-cache",
        "Referer": "https://scoc.fdot.gov/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "ng-api-call": "true",
        "sec-ch-ua": "^\^.Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^"
    }

    response = requests.request("GET", url, data=payload, headers=headers)

    data = response.json()
    df = pd.json_normalize(data)
    return df.to_csv('Florida_projects_tenders.csv')


def getTexasPT():
    url = "https://services.arcgis.com/KTcxiTD9dsQw4r7Z/arcgis/rest/services/TxDOT_Projects/FeatureServer/0/query"

    querystring = {"f":"geojson","where":"1=1","outFields":"*","returnGeometry":"false"}

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)
    data = response.json()
    res = []
    for i in range(len(data.get('features'))):
        res.append(data.get('features')[i].get('properties'))
    df = pd.json_normalize(res)
    return df.to_csv('Florida_projects_tenders.csv')
