import pytest
from project import add_task, remove_task, format_tasks

#test d'ajout
def test_add_task():
    list_test = []
    add_task(list_test, "Coding", "CS50P", 1)
    assert len(list_test) == 1
    assert list_test[0].title == "Coding"

#test de suppression
def test_remove_task():
    list_test = []
    add_task(list_test, "Coding", "CS50P", 1)
    remove_task(list_test, 1)
    assert len(list_test) == 0

def test_format_tasks():
    list_test = []
    #test de liste vide
    assert "no tasks" in format_tasks(list_test).lower()
    
    add_task(list_test, "Coding", "CS50P", 1)
    result = format_tasks(list_test)
    assert "Coding" in result
    assert "CS50P" in result
