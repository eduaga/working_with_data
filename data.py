import json
import xml.etree.ElementTree as ET


def retrieve_news_json(json_file):
    with open(json_file, encoding="utf-8") as f:
        news = json.load(f)
        news_retrieve = news["rss"]["channel"]["items"]
    return news_retrieve

def retrieve_news_from_xml(xml_file):
    parser = ET.XMLParser(encoding="utf-8")
    news_tree = ET.parse(xml_file, parser)
    root = news_tree.getroot()
    news_from_file = root.findall("channel/item/description")
    return news_from_file

def top_ten_from_retrieved_list(retr_list, format):
    top_dict = {}
    words_list = []
    for news in retr_list:
        if format == "json":
            words_list = news["description"].split()
        elif format == "xml":
            words_list = news.text.split()
        for word in words_list:
            word = word.lower()
            if len(word) > 6:
                if word in top_dict:
                    top_dict[word] += 1
                else:
                    top_dict[word] = 1
    for frequency in sorted(top_dict, key=top_dict.get, reverse=True)[0:10]:
        print(f'{frequency} - {top_dict[frequency]} вхождений')



top_ten_from_retrieved_list(retrieve_news_json("newsafr.json"), "json")
#top_ten_from_retrieved_list(retrieve_news_from_xml("newsafr.xml"), "xml")
