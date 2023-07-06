"""Test Python wrapper for Typesense Server"""
import typesense_server


def test_title():
    assert typesense_server.__title__ == 'python-typesense-server-wrapper'


def test_start():
    typesense_server.start()
