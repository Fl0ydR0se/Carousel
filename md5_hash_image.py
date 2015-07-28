from PIL import Image
from hashlib import md5
import io, time


"""


"""

def get_md5_hash(f):
    img = Image.open(f)
    m = md5()
    with io.BytesIO() as memf:
        img.save(memf, 'PNG')
        data = memf.getvalue()
        m.update(data)
    return m.hexdigest()
