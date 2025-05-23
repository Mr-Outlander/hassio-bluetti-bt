# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.
# Bluetti Crypt Module Version: V1.0.0-L

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _bluetti_crypt
else:
    import _bluetti_crypt

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


INT32_MAX = _bluetti_crypt.INT32_MAX
BLUETTI_ERR_SUCCESS = _bluetti_crypt.BLUETTI_ERR_SUCCESS
BLUETTI_ERR_BAD_PARAM = _bluetti_crypt.BLUETTI_ERR_BAD_PARAM
BLUETTI_ERR_PROTO_FMT = _bluetti_crypt.BLUETTI_ERR_PROTO_FMT
BLUETTI_ERR_PROGRAM_INTERVAL = _bluetti_crypt.BLUETTI_ERR_PROGRAM_INTERVAL
BLUETTI_ERR_ECDH_AUTH_FAIL = _bluetti_crypt.BLUETTI_ERR_ECDH_AUTH_FAIL
class BluettiCrypt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _bluetti_crypt.BluettiCrypt_swiginit(self, _bluetti_crypt.new_BluettiCrypt())
    __swig_destroy__ = _bluetti_crypt.delete_BluettiCrypt

    @staticmethod
    def get_instance():
        return _bluetti_crypt.BluettiCrypt_get_instance()

    def ble_crypt_link_handler(self, data):
        return _bluetti_crypt.BluettiCrypt_ble_crypt_link_handler(self, data)

    def encrypt_data(self, data):
        return _bluetti_crypt.BluettiCrypt_encrypt_data(self, data)

    def decrypt_data(self, data):
        return _bluetti_crypt.BluettiCrypt_decrypt_data(self, data)

    def get_software_version(self):
        return _bluetti_crypt.BluettiCrypt_get_software_version(self)

# Register BluettiCrypt in _bluetti_crypt:
_bluetti_crypt.BluettiCrypt_swigregister(BluettiCrypt)

