from bs4 import BeautifulSoup

def readInventory(user):
    html = open(f"./inventory/{user}.html", "r", encoding='utf-8').read()

    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("div", class_="tradehistoryrow")
    events = []
    for row in rows:
        event = row.find("div", class_="tradehistory_event_description").text.replace(
            "                ", "").replace("\n", "")
        items = row.find_all("span", class_="history_item_name")
        # print(items)
        
        try:
            item = items[2].text.replace("                ", "").replace("\n", "").replace("           ", "").replace("\t","")
            if item == None:
                item = items[1].text.replace("                ", "").replace("\n", "").replace("           ", "").replace("\t","")
                if item == None:
                    item = None
        except:
            item = None
        try:
            
            case_name = items[0].text.replace("                ", "").replace("\n", "").replace("           ", "").replace("\t","")
        except:
            case_name = None
            
        event_data = {
            "event": event.replace("\t","").replace("            ",""),
            "case": case_name,
            "item": item

        }
        events.append(event_data)
    return events