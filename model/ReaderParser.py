from xml import sax
from xml.sax import handler
from constants import fields
from Sportsman import Sportsman

class DataHandler(handler.ContentHandler):
    def __init__(self):
        super().__init__()
        self.list = list() 
        self.__currentField = None
        self.__currentRow: dict[str, str] = dict()

    def startElement(self, tag, attrs):
        if tag == "row":
            self.__currentRow = dict()
        else: self.__currentField = tag


    def endElement(self, tag):
        if tag == "row":
            self.list.append(Sportsman(**self.__currentRow))
            self.__currentRow = dict()
        else: self.__currentField = None

    def characters(self, content):
        if self.__currentField == "row":
            return
        elif self.__currentField in fields: self.__currentRow.update({self.__currentField: content})
        


def parseXML(path: str="") -> list[Sportsman]:
    content: str
    with open(path) as xml_file:
        content = xml_file.read()
        handler = DataHandler()
        sax.parseString(content, handler)
    return handler.list


if __name__ == "__main__":
    print(parseXML("../examples/test.xml"))