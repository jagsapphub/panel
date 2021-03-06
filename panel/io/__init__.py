"""
The io module contains utilities for loading JS components, embedding
model state, and rendering panel objects.
"""

import logging

from ..config import config

from .embed import embed_state # noqa
from .state import state # noqa
from .model import add_to_doc, remove_root, diff # noqa
from .resources import Resources # noqa
from .server import get_server, serve, unlocked # noqa
from .notebook import block_comm, ipywidget, load_notebook, push # noqa

panel_logger = logging.getLogger('panel')

if config.log_level is not None:
    panel_logger.setLevel(config.log_level)
