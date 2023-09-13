import re
import requests
import sys
import time


MAX_TREE_LENGTH = 1


def get_links(url, i=0):
    print(url)
    text = requests.get(url).text
    wikipedia_link_list, external_link_list = [], []
    explored = []
    links = re.findall(r'href=[\'"]?([^\'" ]+)', text)
    while i < MAX_TREE_LENGTH:
        wikipedia_links, external_links = _filter_source(links)
        wikipedia_link_list.extend(wikipedia_links)
        external_link_list.extend(external_links)
        for link in wikipedia_links:
            if link not in explored:
                if link[0] == "#":
                    continue
                if link[0] == "/":
                    link = "https://en.wikipedia.org/" + link
                explored.append(link)
                external_link_list.extend(get_links(link, i+1))
        i += 1
    return wikipedia_link_list, external_link_list


def _filter_source(link_list):
    wikipedia_links, external_links = [], []
    for link in link_list:
        if link[0] == "/" or link[0] == "#" or "wiki" in link:
            wikipedia_links.append(link)
        else:
            external_links.append(link)
    return wikipedia_links, external_links


def main():
    pa_wiki = "https://en.wikipedia.org/wiki/Phillips_Academy"
    print("****Getting Links****")
    start_time = time.time()
    wikipedia_links, external_links = get_links(pa_wiki)
    end_time = time.time()
    print("****Links Gotten****")
    print("The number of Wikipedia articles: ", len(wikipedia_links))
    print("The number of external links: ", len(external_links))
    print("*******")
    print("The time taken: ", end_time - start_time)
    print("Tree depth: ", MAX_TREE_LENGTH)
    
    
if __name__ == '__main__':
    main()