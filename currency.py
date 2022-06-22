import pycurl
import certifi
from io import BytesIO

def getURLData(URL):
    #stolen shamelessly from the pycurl documentation site. http://pycurl.io/docs/latest/quickstart.html and edited a little for my own ends.
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, URL)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.perform()
    c.close()
    body = buffer.getvalue()
    # Body is a byte string.
    # We have to know the encoding in order to print it to a text file
    # such as standard output.
    body=body.decode('iso-8859-1')
    return body

def main():
    exchangeDate="latest"
    firstCurrencyCode="eur"
    secondCurrecyCode="gbp"
    finalURL= f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{exchangeDate}/currencies/{firstCurrencyCode}.json"
    URLjson=getURLData(finalURL)
    print(URLjson)

if __name__=="__main__":
    main()
