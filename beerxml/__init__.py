from .models import *  # noqa: F403
from .beerxml_parser import BeerxmlParser  # noqa: F401

__version__ = "0.1.0_anb"
# print custom version on package import
print(f"BeerXML Python version: {__version__}")