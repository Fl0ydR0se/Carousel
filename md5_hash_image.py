from PIL import Image
from hashlib import md5
import io


"""This function calculates and return md5 hash for file.

Usage:
myfile = open(path_to_file, 'rb')
print get_md5_hash(myfile)

"""

def get_md5_hash(f):
    img = Image.open(f)
    m = md5()
    with io.BytesIO() as memf:
        img.save(memf, 'PNG')
        data = memf.getvalue()
        m.update(data)
    return m.hexdigest()
