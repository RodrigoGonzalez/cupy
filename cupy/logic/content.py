from cupy import core


def _create_float_test_ufunc(name, doc):
    return core.create_ufunc(
        f'cupy_{name}',
        ('e->?', 'f->?', 'd->?'),
        f'out0 = {name}(in0)',
        doc=doc,
    )


isfinite = _create_float_test_ufunc(
    'isfinite',
    '''Tests finiteness elementwise.

    Each element of returned array is ``True`` only if the corresponding
    element of the input is finite (i.e. not an infinity nor NaN).

    .. seealso:: :data:`numpy.isfinite`

    ''')


isinf = _create_float_test_ufunc(
    'isinf',
    '''Tests if each element is the positive or negative infinity.

    .. seealso:: :data:`numpy.isinf`

    ''')


isnan = _create_float_test_ufunc(
    'isnan',
    '''Tests if each element is a NaN.

    .. seealso:: :data:`numpy.isnan`

    ''')


# TODO(okuta): Implement isneginf


# TODO(okuta): Implement isposinf
