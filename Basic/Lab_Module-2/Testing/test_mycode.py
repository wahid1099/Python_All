import mycode 


api_url="https://api.nasa.gov/planetary/apod?api_key=7RkWu7DfDbdIWbQF8ByK5EAv8IfbphLwEfUygAmA"


def test_get_response():
    ret=mycode.get_response(api_url)
    assert ret.status_code==200


def test_sum():
    assert 3==3

# for running tesign we have to write =="python -m pytest"