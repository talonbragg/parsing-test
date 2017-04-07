# coding=utf-8

# This file contains the command line interface to the METAR decoder you have built. It instantiates the METAR decoder, then performs the following actions:
#
# 1) opens the metar file submitted to it under the --source attribute,
# 2) opens the file and iterates it row-wise,
# 3) passes each to the decoder object `MetarDecoder`'s `decode()` method line by line,
# 4) calls the `dict_export()` method on your `MetarResult` object,
# 5) aggregates the results,
# 6) serialises them to Avro.

import click
from fastavro import writer
from src.decoder import MetarDecoder
from src.schema import metar

@click.command()
@click.option('--source', '-i', help="Source file path")
@click.option('--output', '-o', help="Output file path")
def parse(source, output):
    """Parses a .metar file, containing a metar telegram for each line, to an Avro file using the included schema."""

    # An array of dicts to comprise all parsed outputs. The dicts have to comply with the Avro schema
    results = []

    # Initialise the parser
    parser = MetarDecoder()

    with open(source) as input_file:
        line = input_file.readline()
        results.append(parser.decode(line))

    with open(output) as output_file:
        writer(output_file, metar, results)

    print("Parsing complete, {} records written to {}.".format(len(results), output))
