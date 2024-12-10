import tic_tac_toe_1d

def test_evaluate_x_wins():
    assert tic_tac_toe_1d.evaluate('---xxx---oo--') == 'x'

def test_evaluate_o_wins():
    assert tic_tac_toe_1d.evaluate('---xx---ooo--') == 'o'

def test_evaluate_no_wins():
    assert tic_tac_toe_1d.evaluate('xoxxooxoxx') == '!'

def test_evaluate_no_wins_yet():
    assert tic_tac_toe_1d.evaluate('---xx---oo--') == '-'

def test_move_to_first():
    assert tic_tac_toe_1d.move('---', 'o', 0) == 'o--'

def test_move_to_last():
    assert tic_tac_toe_1d.move('---', 'o', 2) == '--o'

def test_move_to_middle():
    assert tic_tac_toe_1d.move('---', 'x', 1) == '-x-'



# What is a Python module and how does it differ from a Python package? 
# A module is basically a python file, containing python code, function and expressions. This module can be imported to other codes. 
# Package is a type of module which is a selection of modules all connected together in functionality.

# What are side effects and give some examples.
# When importing a module results in some kind of action other than the import. It can be anything from a print statement, running a program to the apperance of a pop up window

# What are Exceptions and what to do if third-party code that we use throws them?
# Exceptions are basically error messages to show what type of problem the code has.
# We should check the Exception, if we can avoid it the next time then we should. If we cannot avoid it then we could try to handle it so that our own user understands the Exception.

# Using which keywords can you create, throw and catch your new custom Exception?
# Exception(), ValueError()... creates a new exception
# raise throws an exception
# and except catches the exception 

# Give examples of some benefits of testing?
# You can realise if something is not working as intended in your code
# You don't have to test it over and over again manually when editing the code, but use the same test file for that