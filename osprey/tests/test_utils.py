from __future__ import print_function, absolute_import, division
import os
from os.path import samefile, abspath
import tempfile
import datetime
from osprey.utils import dict_merge, in_directory
from osprey.utils import format_timedelta, current_pretty_time
from osprey.utils import is_json_serializable
import numpy as np
from sklearn.base import BaseEstimator

def test_is_json_serializable():
    a = BaseEstimator()
    b = np.array([1, 2, 3], dtype=int)
    c = np.array([1., 2., 3.], dtype=float)
    d = np.array(['a', 'b', 'c'], dtype=str)
    e = ['a', 'b', 'c']
    f, g, h, i = None, True, 1, 1.2
    for obj in [a, b, c, d]:
        assert(~is_json_serializable(obj))
    for obj in [e, f, g, h, i]:
        assert(is_json_serializable(obj))

def test_dict_merge_1():
    base = {'a': 1}
    top = {'a': 2}
    assert dict_merge(base, top) == top


def test_dict_merge_2():
    base = {'a': 1}
    top = {'a': 2, 'b': 3}
    assert dict_merge(base, top) == top


def test_dict_merge_3():
    base = {'a': 1, 'b': 2}
    top = {'a': 2}
    assert dict_merge(base, top) == {'a': 2, 'b': 2}


def test_dict_merge_4():
    base = {'a': {'a': 1}, 'b': {'b': 2}}
    top = {'a': {'a': 2, 'b': 3}}
    assert dict_merge(base, top) == {'a': {'a': 2, 'b': 3}, 'b': {'b': 2}}


def test_in_directory_1():
    tempdir = tempfile.mkdtemp()
    try:
        initialdir = abspath(os.curdir)
        with in_directory(tempdir):
            assert samefile(abspath(os.curdir), tempdir)
        assert samefile(abspath(os.curdir), initialdir)
    finally:
        os.rmdir(tempdir)


def test_format_timedelta():
    print(format_timedelta(datetime.timedelta(seconds=413302.33)))


def test_current_pretty_time():
    print(current_pretty_time())
