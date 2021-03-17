from mopidy_vfd import Extension


def test_get_default_config():
    ext = Extension()

    config = ext.get_default_config()

    assert "[vfd]" in config
    assert "enabled = true" in config


def test_get_config_schema():
    ext = Extension()

    schema = ext.get_config_schema()

    assert "display" in schema
