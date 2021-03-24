# Copyright (c) 2019-2021, Jonas Eschle, Jim Pivarski, Eduardo Rodrigues, and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/vector for details.

import pytest

import vector
import vector.backends.object_

numba = pytest.importorskip("numba")


import vector.backends.numba_numpy  # noqa: E402


def test_pass_through():
    @numba.njit
    def pass_through(obj):
        return obj

    array = vector.array({"px": [1, 2, 3], "py": [10, 20, 30]})
    assert isinstance(array, vector.backends.numpy_.VectorNumpy)
    assert isinstance(pass_through(array), vector.backends.numpy_.VectorNumpy)