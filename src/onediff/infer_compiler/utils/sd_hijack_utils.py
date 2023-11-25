"""Hijack utils for stable-diffusion."""
from types import FunctionType
from typing import Union, Callable
import importlib
import inspect

__all__ = ["hijack_func", "is_hijacked"]


def get_func_full_name(func: FunctionType):
    """Get the full name of a function."""
    module = inspect.getmodule(func)
    if module is None:
        raise ValueError(f"Cannot get module of function {func}")
    return f"{module.__name__}.{func.__qualname__}"


class CondFunc:
    """A function that conditionally calls another function. 

    Copied from: https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/modules/sd_hijack_utils.py
    """

    def __new__(cls, orig_func, sub_func, cond_func):
        # self: CondFunc instance
        self = super(CondFunc, cls).__new__(cls)
        if isinstance(orig_func, str):
            func_path = orig_func.split(".")
            for i in range(len(func_path) - 1, -1, -1):
                try:
                    resolved_obj = importlib.import_module(".".join(func_path[:i]))
                    break
                except ImportError:
                    pass
            for attr_name in func_path[i:-1]:
                resolved_obj = getattr(resolved_obj, attr_name)
            orig_func = getattr(resolved_obj, func_path[-1])
            setattr(
                resolved_obj,
                func_path[-1],
                lambda *args, **kwargs: self(*args, **kwargs),
            )

            def unhijack_func():
                setattr(resolved_obj, func_path[-1], orig_func)

        self.__init__(orig_func, sub_func, cond_func)
        return (lambda *args, **kwargs: self(*args, **kwargs), unhijack_func)

    def __init__(self, orig_func, sub_func, cond_func):
        self.__orig_func = orig_func
        self.__sub_func = sub_func
        self.__cond_func = cond_func

    def __call__(self, *args, **kwargs):
        if not self.__cond_func or self.__cond_func(self.__orig_func, *args, **kwargs):
            return self.__sub_func(self.__orig_func, *args, **kwargs)
        else:
            return self.__orig_func(*args, **kwargs)


def is_hijacked(func: Callable, *, use_cond_func: Callable = None):
    """Check if a function is hijacked."""
    func_path = get_func_full_name(func)
    if use_cond_func is None:
        cond_func_path = get_func_full_name(CondFunc)
    else:
        cond_func_path = get_func_full_name(cond_func)

    expected_path = f"{cond_func_path}.__new__.<locals>.<lambda>"
    return func_path == expected_path


def hijack_func(
    orig_func: Union[str, Callable], sub_func: Callable, cond_func: Callable
):
    """
    Hijacks a function with another function.  

    Returns: 
        A tuple of (hijacked_func, unhijack_func)

    Examples:
        >>> def foo(*args, **kwargs):
        >>>     # orig_func
        >>>     print('foo')
        >>> def bar(orig_func, *args, **kwargs):
        >>>     # sub_func
        >>>     print('bar')
        >>> def cond_func(orig_func, *args, **kwargs):
        >>>     # cond_func
        >>>     return True
        >>> hijack_func(foo, bar, cond_func)
        >>> foo()
        bar
    """

    if isinstance(orig_func, FunctionType):
        orig_func = get_func_full_name(orig_func)
    return CondFunc(orig_func, sub_func, cond_func)
