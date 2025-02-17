"""Module to convert PyTorch code to OneFlow."""
from .manager import transform_mgr
from .builtin_transform import torch2oflow, default_converter
from .custom_transform import register

from .builtin_transform import (
    ProxySubmodule,
    proxy_class,
    replace_obj,
    map_args,
    replace_func,
    get_attr,
)
