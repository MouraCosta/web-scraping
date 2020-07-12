import requests
from concurrent.futures import ThreadPoolExecutor
from plotly.offline import offline


def get_data(id_, artc: list, descd: list, by: list):
    """Get the data and append to the respective lists.

        lists = article_links, descendants, by
        id_ --> var caught in a for loop"""

    # Make an API call to stores the results
    url = f'https://hacker-news.firebaseio.com/v0/item/{id_}.json'
    r = requests.get(url)
    current_dict = r.json()
    print(f'{id_}: {r.status_code}'
          .replace('200', '\033[;36mOk\033[m'))

    # Do a treatment to check if the "url" key exists
    try:
        artc.append(f"<a href='{current_dict['url']}'>"
                 f"{current_dict['title']}'</a>")
        descd.append(current_dict['descendants'])
        by.append(f'article by:{current_dict["by"]}')
    except KeyError as key:
        print(f"The key {key} is missing in the {id_}"
              f" information")


def main():
    """Principal Program.
    Make a visualization about views in each article."""

    # Make an API call and stores the id's
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    req = requests.get(url)
    id_list = req.json()[:30]  # Only 30 results
    print(f"PRINCIPAL STATUS CODE: {req.status_code}"
          .replace('200', '\033[;36mOk\033[m'))

    # Threading for faster results
    article_links, descendants, by = [], [], []
    with ThreadPoolExecutor() as executor:
        for id_ in id_list:
            executor.submit(get_data, id_, article_links, 
                            descendants, by)

    # Make a visualization with the obtained data from an API call
    data = {
        'type': 'bar', 
        'x': article_links, 
        'y': descendants,
        'hovertext': by,
        'marker': {
            'color': 'rgb(125, 0, 0)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.8
    }
    my_layout = {
        'title': 'Top 10 most viewed articles',
        'titlefont': {'size': 24},
        'xaxis': {
            'title': 'Articles',
            'titlefont': {'size': 12}
        },
        'yaxis': {
            'title': 'Views',
            'titlefont': {'size': 12}
        }
    }
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='Most visited article.html')


if __name__ == '__main__':
    main()
