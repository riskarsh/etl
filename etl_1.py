#!/usr/bin/python3
from abc import abstractmethod
from abc import ABC
from typing import List
import sys

class Reader(ABC):
    @abstractmethod
    def read(self):
        raise NotImplemented

class Transformer(ABC):
    @abstractmethod
    def transform(self, data):
        raise NotImplemented

class Writer(ABC):
    @abstractmethod
    def write(self, data):
        raise NotImplemented

class ETLPipeline:
    def __init__(self, reader: Reader , transformers: List[Transformer], writer: Writer) -> None:
        self.reader = reader
        self.transformers = transformers
        self.writer = writer
    
    def run(self):
        data = self.reader.read()
        for transformer in self.transformers:
            data= transformer.transform(data)
        self.writer.write(data)    

class FileReader(Reader):
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def read(self):
        with open(self.filepath) as fd:
            return fd.read()

class TransfromUpper(Transformer):
    def transform(self, data):
        return data.upper()

class FileWriter(Writer):
    def __init__(self,filepath) -> None:
        self.filepath = filepath

    def write(self, data):
        with open(self.filepath, 'w') as fw:
            fw.write(data)


def main(args):
    if len(args) < 3:
        print('Usage: etl.py <input filepath> <output filepath>')
        exit()

    inputfile = args[1]
    outputfile = args[2]
    freader = FileReader(inputfile)
    fwriter = FileWriter(outputfile)
    pipeline = ETLPipeline(
        reader = freader,
        transformers = [TransfromUpper(),],
        writer = fwriter,
     )
    pipeline.run()

main(sys.argv)