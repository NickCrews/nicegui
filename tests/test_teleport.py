from typing import Optional

from nicegui import ui
from nicegui.testing import SeleniumScreen


def test_teleport(screen: SeleniumScreen):
    ui.card().classes('card')

    def create_teleport():
        with ui.teleport('.card'):
            ui.label('Hello')

    ui.button('create', on_click=create_teleport)

    screen.open('/')
    screen.click('create')
    assert screen.find_by_css('.card > div').text == 'Hello'


def test_teleport_with_element(screen: SeleniumScreen):
    card = ui.card().classes('card')

    def create_teleport():
        with ui.teleport(card):
            ui.label('Hello')

    ui.button('create', on_click=create_teleport)

    screen.open('/')
    screen.click('create')
    assert screen.find_by_css('.card > div').text == 'Hello'


def test_update(screen: SeleniumScreen):
    teleport: Optional[ui.teleport] = None

    card = ui.card().classes('card')

    def create_teleport():
        nonlocal teleport
        with ui.teleport('.card') as teleport:
            ui.label('Hello')

    ui.button('create', on_click=create_teleport)

    def rebuild_card():
        card.delete()
        ui.card().classes('card')
        teleport.update()  # type: ignore

    ui.button('rebuild card', on_click=rebuild_card)

    screen.open('/')
    screen.click('create')
    screen.should_contain('Hello')
    screen.click('rebuild card')
    assert screen.find_by_css('.card > div').text == 'Hello'
