from cStringIO import StringIO
from gzip import GzipFile

def gunzip(data):
    """Gunzip the given data and return as much data as possible.

    This is resilient to CRC checksum errors.
    """
    f = GzipFile(fileobj=StringIO(data))
    output = ''
    chunk = '.'
    while chunk:
        try:
            chunk = f.read(8196)
            output += chunk
        except IOError:
            # complete only if there is some data, otherwise re-raise
            if output:
                output += f.extrabuf
                break
            else:
                raise
    return output
