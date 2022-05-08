from collections import defaultdict
import sys
from etl_1 import FileReader, FileWriter, Transformer, ETLPipeline

class WordCounter(Transformer):
    """Applies the transformation and counts the occurences of the words in the text.
    """

    def transform(self, data):
        for char in [",", ".", "-", ";", "!"]:
            data = data.replace(char, "")
        counter = defaultdict(int)
        for word in data.split():
            counter[word.lower()] += 1
        output = ""

        for word, count in counter.items():
            output += f"{word} -> {count} \n"
        return output


def main(args):
    """Main function that takes the filepath as a first system argument,
    output filedestination as second system argument.
    """
    if len(args) < 3:
        print("Usage: etl_2.py <input filepath> <output filepath>")
        exit()

    inputfile = args[1]
    outputfile = args[2]
    freader = FileReader(inputfile)
    fwriter = FileWriter(outputfile)
    pipeline = ETLPipeline(
        reader=freader, 
        transformers=[WordCounter()], 
        writer=fwriter,)
    pipeline.run()

main(sys.argv)