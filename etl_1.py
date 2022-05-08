#!/usr/bin/python3
from abc import abstractmethod, ABC
from typing import List
import sys


class Reader(ABC):
    """A simple reader interface that reads from a given source.
    """

    @abstractmethod
    def read(self):
        raise NotImplemented


class Transformer(ABC):
    """A simple transformer interface that applies the transformations.
    """

    @abstractmethod
    def transform(self, data):
        raise NotImplemented


class Writer(ABC):
    """A simple writer interface that writes to a given destination.
    """

    @abstractmethod
    def write(self, data):
        raise NotImplemented


class ETLPipeline:
    """Handles the actual ETL process.
    Takes the reader, transformers and writer as input.
    It reads data from reader, passes it to all the transformers and finally sends it to the writer.
    """

    def __init__(
        self, reader: Reader, transformers: List[Transformer], writer: Writer
    ) -> None:
        self.reader = reader
        self.transformers = transformers
        self.writer = writer

    def run(self):
        data = self.reader.read()
        for transformer in self.transformers:
            data = transformer.transform(data)
        self.writer.write(data)


class FileReader(Reader):
    """Reads the file from the filepath and reads the content of the file.
    """

    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def read(self):
        with open(self.filepath) as fd:
            return fd.read()


class TransfromUpper(Transformer):
    """Applies the transformation.
    Capitalizes the content of the file.
    """
    
    def transform(self, data):
        return data.upper()


class FileWriter(Writer):
    """Writes the file to the specified path.
    """

    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def write(self, data):
        with open(self.filepath, "w") as fw:
            fw.write(data)


def main(args):
    """Main function that takes the filepath as a first system argument,
    output filedestination as second system argument.
    """
    if len(args) < 3:
        print("Usage: etl_1.py <input filepath> <output filepath>")
        exit()

    inputfile = args[1]
    outputfile = args[2]
    freader = FileReader(inputfile)
    fwriter = FileWriter(outputfile)
    pipeline = ETLPipeline(
        reader=freader, 
        transformers=[TransfromUpper()], 
        writer=fwriter,
    )
    pipeline.run()

main(sys.argv)