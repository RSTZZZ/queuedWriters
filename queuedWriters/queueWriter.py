from abc import ABC, abstractmethod
from collections import deque
from loguru import logger
import os


class QueueWriter(ABC):
    '''
    Abstract class to have a queue of information to write.

    Users append information to the queue. 
    Once the amount of information in the queue reaches max size, it will automatically flush into the file_name provided.
    Call flush() at the very end for any remaining information.
    '''

    def __init__(self, name: str, file_name: str, buffer_size: int, overwrite_file: bool):
        '''
        Initializes the queue.

        Parameters
        ----------
        name: int
            The name for this queue. Used for logging.
        file_name: str
            The file name to write the information added to this queue.
        buffer_size: int
            The size the queue can grow to before it is flushed into the `file_name`
        overwrite_file: bool
            Whether to overwrite `file_name` or not.


        Returns
        -------
        QueueWriter
        '''
        self.name = name
        self.file_name = file_name
        self.results = deque()
        self.max_size = buffer_size

        if (overwrite_file and os.path.exists(file_name)):
            os.remove(file_name)

    def append(self, info: str):
        '''
        Appends to queue. If the size of the queue is equal to the max_size, it will flush the content before appending.

        Parameters
        ----------
        info: str
            The string to append to the queue.

        Returns
        -------
        None
        '''
        if (len(self.results) == self.max_size):
            self.flush()

        self.results.append(info)

    @abstractmethod
    def flush(self):
        '''
        Flushes the queue by appending everything in the queue to the `file_name`.

        Returns
        -------
        None
        '''
        pass
