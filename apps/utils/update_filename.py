import hashlib
import datetime
import os

from functools import partial
from uuid import uuid4


def path_and_rename(instance,filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.user.id}_{instance.phone}.{datetime.date}.{ext}"
    
    return os.path.join('uploads',filename)
    
    
