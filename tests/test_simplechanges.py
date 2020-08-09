from simplechanges import __version__, SimpleChangesParser


def test_version():
    assert __version__ == '0.1.0'


def test_parsing():
    parsed = SimpleChangesParser("sample.changes")
    parsed.parse()
    assert parsed.latest[0] == "v1.0.1"
