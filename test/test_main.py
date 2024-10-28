import src.main


def test_hello(capfd):
    ret_code = src.main.olbutt("hello")
    assert ret_code == 0
    captured = capfd.readouterr()
    assert captured.out.strip() == "hello world"
