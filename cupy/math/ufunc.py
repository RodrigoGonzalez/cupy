from cupy import core


def create_math_ufunc(math_name, nargs, name, doc):
    assert 1 <= nargs <= 2
    if nargs == 1:
        return core.create_ufunc(
            name, ('e->e', 'f->f', 'd->d'), f'out0 = {math_name}(in0)', doc=doc
        )
    else:
        return core.create_ufunc(
            name,
            ('ee->e', 'ff->f', 'dd->d'),
            f'out0 = {math_name}(in0, in1)',
            doc=doc,
        )
