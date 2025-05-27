from main import damage_taken
def test_1():
    assert damage_taken(5,5)==1
def test_2():
    assert damage_taken(20,5)==15
def test_3():
    assert damage_taken(18,3)==15
def test_4():
    assert damage_taken(1,4)==0
# lai testi stradātu jaievada pytest test.py un jāaizvert logu divas reizes :)
