import sys
sys.path += ['../src']
from sample import *
import pytest
import io


def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bruce,wayne2wayneenterprises,com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('brucewayne@wayneenterprises,com'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bruce.wayne@wayneenterprisescom'))
    assert get_email_from_input() == 'bruce.wayne@wayneenterprisescom'


