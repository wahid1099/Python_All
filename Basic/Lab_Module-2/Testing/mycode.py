import  requests

api_url="https://api.nasa.gov/planetary/apod?api_key=7RkWu7DfDbdIWbQF8ByK5EAv8IfbphLwEfUygAmA"


def get_response(url):
    return requests.get(url)


if __name__=="__main__":
    res=get_response(api_url)
    print(res)