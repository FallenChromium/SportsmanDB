import xml.dom.minidom as minidom

def writeXML(filepath, dataList: list):
    document = minidom.Document()
    rootNode = document.createElement("table")
    document.appendChild(rootNode)

    for record in [record.__dict__ for record in dataList]:
        rowNode = document.createElement("row")
        rootNode.appendChild(rowNode)

        for tagName in record.keys():
            node = document.createElement(tagName)
            content = document.createTextNode(str(record[tagName]))
            node.appendChild(content)
            rowNode.appendChild(node)

    with open(filepath, "w", encoding="UTF-8") as file:
        document.writexml(file, addindent='    ', newl='\n', encoding='UTF-8')