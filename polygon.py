import requests
from html.parser import HTMLParser
#import keys

version = 0.001

explorerUrl = "https://polygonscan.com/"


# contractPageData = []


class polygonScanParser(HTMLParser):
    # i = []
    contractPageData = []

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag:", tag)
        pass

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        # self.output(data)
        self.contractPageData.append(data)
        # return data


def run(w3):
    print(version)


def html_to_list(rawHtml, parser):
    # pass the raw HTML to HTMLParser
    parser.feed(rawHtml)



def get_url_trailer(addrtype):
    if addrtype == "address":
        return "code"
    if addrtype == "token":
        return "readContract"
    pass

def get_abi(w3, addrType, contractAddr):
    url_trailer = get_url_trailer(addrType)
    url = explorerUrl + addrType + "/" + contractAddr + "#" + url_trailer
    r = requests.get(url=url)
    parser = polygonScanParser()
    html_to_list(r.text, parser)
    for i in parser.contractPageData:
        if "inputs\":[]," in i:
            result = i

    return result

if __name__ == '__main__':
    w3 = "Testing"
    contractAddr = "0xdc9232e2df177d7a12fdff6ecbab114e2231198d"
    run(w3)
