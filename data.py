import json


def retrieve_news_json(json_file):
    with open(json_file, encoding="utf-8") as f:
        news = json.load(f)
        news_retrieve = news["rss"]["channel"]["items"]
    return news_retrieve

def top_ten_from_retrieved_list(retr_list):
    top_dict = {}
    words_list = []
    for news_blocks in retr_list:
        words_list = news_blocks["description"].split()
        for word in words_list:
            if len(word) > 6:
                if word in top_dict:
                    top_dict[word] += 1
                else:
                    top_dict[word] = 1
    print(f'Список наиболее популярных вхождений в тексте:\n{sorted(top_dict, key=top_dict.get, reverse=True)[0:10]}')





top_ten_from_retrieved_list(retrieve_news_json("newsafr.json"))
