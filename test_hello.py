from hello import print_hello

def test_print_hello(capsys):
    print_hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World !"