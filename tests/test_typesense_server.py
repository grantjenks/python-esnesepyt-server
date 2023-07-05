"""Test Python wrapper for Typesense Server"""
import pytest
import typesense_server


def test_title():
    assert typesense_server.__title__ == 'python-esnesepyt-server'


def test_start():
    typsense_server.start()
