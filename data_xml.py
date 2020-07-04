import xml.etree.ElementTree as ET


def retrieve_news_from_xml(xml_file):
    parser = ET.XMLParser(encoding="utf-8")
    news_tree = ET.parse(xml_file, parser)
    root = news_tree.getroot()
    news_from_file = root.findall("channel/item/description")
    return news_from_file



def top_ten_from_retrieved_list(retr_list):
    top_dict = {}
    words_list = []
    for news in retr_list:
        words_list = news.text.split()
        for word in words_list:
            if len(word) > 6:
                if word in top_dict:
                    top_dict[word] += 1
                else:
                    top_dict[word] = 1
    print(f'Список наиболее популярных вхождений в тексте:\n{sorted(top_dict, key=top_dict.get, reverse=True)[0:10]}')


top_ten_from_retrieved_list(retrieve_news_from_xml("newsafr.xml"))