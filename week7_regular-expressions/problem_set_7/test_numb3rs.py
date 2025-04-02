from numb3rs import validate_IP


def test_valid():
    assert validate_IP("127.0.0.1") == True
    assert validate_IP("255.255.255.255") == True
    assert validate_IP("169.169.169.169") == True
    assert validate_IP("1.11.111.211") == True
    assert validate_IP("0.99.199.251") == True


def test_invalid():
    assert validate_IP("512.512.512.512") == False
    assert validate_IP("1.2.3.1000") == False
    assert validate_IP("275.3.6.28") == False
    assert validate_IP("192.168.01.1") == False
    assert validate_IP("cat") == False
