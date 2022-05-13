import pytest
from babel.page import Page, InvalidPageException, InvalidPageTextException


def test_get_page_error_handling():
	"""Test the error handling in the get_page function"""
	with pytest.raises(InvalidPageException):
		Page("", 1, 1, 1, 1).content()
	with pytest.raises(InvalidPageException):
		Page("0", 0, 1, 1, 1).content()
	with pytest.raises(InvalidPageException):
		Page("0", 1, 0, 1, 1).content()
	with pytest.raises(InvalidPageException):
		Page("0", 1, 1, 0, 1).content()
	with pytest.raises(InvalidPageException):
		Page("0", 1, 1, 1, 0).content()

def test_find_text_error_handling():
	"""Test the error handling of find_text()"""
	with pytest.raises(InvalidPageTextException):
		Page.find_text("123")
	with pytest.raises(InvalidPageTextException):
		Page.find_text("a"*3201)
