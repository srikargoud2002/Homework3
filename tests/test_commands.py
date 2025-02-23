"""Tests for the greet class."""

import pytest
from app import App
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand

def test_greet_command(capfd):
    """Tests for the greet class."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()  # Ignore 'err' since it's not used
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    """Tests for the goodbye class."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()  # Ignore 'err' since it's not used
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
