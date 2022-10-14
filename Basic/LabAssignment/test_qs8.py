import qs8


text="hi  HOW are YOU"



def test_make_lower():
    ret=qs8.make_lower(text)
    assert ret.islower() == True



def test_make_upper():
    ret=qs8.make_upper(text)
    assert ret.isupper() == True



def test_make_capital():
    ret=qs8.make_capital(text)
    assert ret.istitle() == True

