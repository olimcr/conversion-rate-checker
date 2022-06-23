import pycurl
import certifi
import re
from io import BytesIO
#https://github.com/fawazahmed0/currency-api#readme
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

def findSecondCurrencyCode(URLjson,secondCurrecyCode):
    for line in URLjson.split("\n"):
        line=re.search(secondCurrecyCode+r'.*', URLjson)
    return line.group()

def cleanURLData(URLjson):
    URLjson= re.sub(r'"', "", URLjson)
    URLjson= re.sub(r',', "", URLjson)
    URLjson= re.sub(r'{\n\s*.*\n\s*.*', "", URLjson)
    URLjson= re.sub(r'.*}\n.*', "", URLjson)
    return URLjson

def main():
    exchangeDate=input("Enter a date in (yyyy-mm-dd) format. leave blank for latest data: ")
    if exchangeDate=="":
        exchangeDate="latest"
    firstCurrencyCode=input("Enter first currency shortcode(eg:usd,gbp,cad): ")
    currencyAmount=input("Enter the amount of currency to convert: ")
    secondCurrecyCode=input("Enter second currency shortcode: ")
    if(firstCurrencyCode==secondCurrecyCode):
        print(f"at {exchangeDate} {currencyAmount} {firstCurrencyCode} is worth {currencyAmount} {secondCurrecyCode}")
        exit()
    finalURL= f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{exchangeDate}/currencies/{firstCurrencyCode}.json"
    URLjson=getURLData(finalURL)
    URLjson=cleanURLData(URLjson)
    line=findSecondCurrencyCode(URLjson,secondCurrecyCode)
    line=re.sub(r'.+:\W', "", line)
    convertedCurrency=float(line)*int(currencyAmount)
    convertedCurrency=round(convertedCurrency,2)
    print(f"at {exchangeDate} {currencyAmount} {firstCurrencyCode} is worth {convertedCurrency} {secondCurrecyCode}")

if __name__=="__main__":
    main()
