import pytest

from app.slugify import slugify


def test_basic():
    assert slugify("Hello, CI World!") == "hello-ci-world"


def test_collapses_whitespace_and_symbols():
    assert slugify("  multiple   spaces  ") == "multiple-spaces"
    assert slugify("a!!!b???c") == "a-b-c"


def test_unicode_folds_to_ascii():
    assert slugify("café över") == "cafe-over"


def test_already_clean():
    assert slugify("already-clean") == "already-clean"


def test_empty_string():
    assert slugify("") == ""


def test_numeric_input_string():
    assert slugify("123") == "123"
    assert isinstance(slugify("123"), str)
