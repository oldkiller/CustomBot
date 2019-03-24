import sys
sys.path.append("..")

from importlib import import_module
from importlib import resources

from bot import bot

bot = bot

PLUGINS = dict()

def plugin(func):
    name = func.__name__
    PLUGINS[name] = func
    return func

def __getattr__(name):
    try:
        return PLUGINS[name]
    except KeyError:
        _import_plugins()
        if name in PLUGINS:
            return PLUGINS[name]
        else:
            raise AttributeError(
                f"module {__name__!r} has no attribute {name!r}"
            ) from None
 
def __dir__():
    _import_plugins()
    return list(PLUGINS.keys())
 
def _import_plugins():
    for name in resources.contents(__name__):
        if name.endswith(".py"):
            import_module(f"{__name__}.{name[:-3]}")

def run():
    _import_plugins()