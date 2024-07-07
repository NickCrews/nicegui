import importlib

from nicegui.testing import Screen

from .. import main

# pylint: disable=missing-function-docstring


def test_markdown_message(screen: Screen) -> None:
    importlib.reload(main)

    screen.open('/')
    screen.should_contain('Try running')


def test_button_click(screen: Screen) -> None:
    importlib.reload(main)

    screen.open('/')
    screen.click('Click me')
    screen.should_contain('Button clicked!')


def test_sub_page(screen: Screen) -> None:
    importlib.reload(main)

    screen.open('/subpage')
    screen.should_contain('This is a subpage')


def test_with_connected(screen: Screen) -> None:
    importlib.reload(main)

    screen.open('/with_connected')
    screen.should_contain('This is an async connection demo')
    screen.should_contain('Connected!')


def test_navigation(screen: Screen) -> None:
    importlib.reload(main)

    screen.open('/')
    screen.click('go to subpage')
    screen.should_contain('This is a subpage')
