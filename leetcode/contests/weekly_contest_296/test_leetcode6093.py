from .leetcode6093 import TextEditor


def test_text_editor():
    text_editor = TextEditor()
    text_editor.addText("leetcode")

    assert text_editor.deleteText(4) == 4

    text_editor.addText("practice")

    assert "".join(text_editor.stack) == "leetpractice|"

    assert text_editor.cursorRight(3) == "etpractice"

    assert text_editor.cursorLeft(8) == "leet"

    assert text_editor.deleteText(10) == 4

    assert text_editor.cursorLeft(2) == ""

    assert text_editor.cursorRight(6) == "practi"


def test_text_editor2():
    text_editor = TextEditor()
    text_editor.addText("woyrgb")

    assert text_editor.cursorLeft(1) == "woyrg"
    assert text_editor.cursorRight(20) == "woyrgb"
