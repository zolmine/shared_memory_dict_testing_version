from unicodedata import name
from shared_memory_dict import SharedMemoryDict

shared = SharedMemoryDict(name='shared', size=1024)