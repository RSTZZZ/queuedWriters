# QueuedWriters

A group of writers that uses python's `dequeue` to queue appropriate information. Once the queue reaches the max `buffer_size`, it will automatically flush the `dequeue` to the provided `file_name` before continuing to append to the `dequeue`

## Supported Files

- JSON: Instead of having the whole file as a proper JSON object, each line is a proper JSON object.
- CSV: Standard CSV file.
