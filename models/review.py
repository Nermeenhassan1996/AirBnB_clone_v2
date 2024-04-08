#!/usr/bin/python3
"""Review class
"""

import uuid
from datetime import datetime
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class """
    place_id = ""
    user_id = ""
    text = ""
