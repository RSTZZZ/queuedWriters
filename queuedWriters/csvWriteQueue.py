import csv
from loguru import logger

from queuedWriters.queueWriter import QueueWriter


class CSVQueueWriter(QueueWriter):
    '''
    A CSV writer that is queued. Once the queue reaches its buffer_size, it will flush all contents to the associated file.

    Examples
    --------
    The following shows the format of the csv file that is written.

    >>> header = ["column_1", "column_2", "column_3"]
    >>> rows = [["a", "a", "a"]] * 5
    >>> testCSVWriter = CSVQueueWriter("test", "./test.csv", 2, True)
    >>> testCSVWriter.append(header)
    >>> for row in rows:
        testCSVWriter.append(row)
    >>> testCSVWriter.flush()
    '''

    def flush(self):
        logger.debug(
            f"{self.name}: Flushing {len(self.results)} into {self.file_name}.")
        with open(self.file_name, "a",  newline='') as result_file:
            csv_writer = csv.writer(result_file)
            while self.results:
                row = self.results.popleft()
                csv_writer.writerow(row)
