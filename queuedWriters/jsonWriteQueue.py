import json
from loguru import logger

from queuedWriters.queueWriter import QueueWriter


class JSONQueueWriter(QueueWriter):
    '''
    Writer to generate a json per line. (JSON like file)

    Examples
    --------
    The following shows the format of the json-like file that is written.

    >>> info = [{"a" : "a"}, {"a" : "a"}， {"a" : "a"}， {"a" : "a"}]
    >>> testQueue = JSONQueueWriter("jsonQueue", "./test.json", 2, True)
    >>> for i in info:
            testQueue.append(i)
    >>> testQueue.flush()

    Resulting `test.json` file:
    {"a" : "a"}
    {"a" : "a"}
    {"a" : "a"}
    {"a" : "a"}
    '''

    def flush(self):
        logger.debug(
            f"{self.name}: Flushing {len(self.results)} into {self.file_name}.")
        with open(self.file_name, "a", newline="", encoding="utf-8") as result_file:
            while self.results:
                row = self.results.popleft()
                json_row = json.dumps(row, default=str) + "\n"
                result_file.write(json_row)
