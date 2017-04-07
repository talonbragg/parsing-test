METAR decoder
-------------

This test task asks you to create a METAR decoder that ingests a ``.metar`` file, comprising METAR observations (one observation per line), parse them and serialise them to an Avro schema. Your code should be callable from ``src/cli.py`` without alterations.

Task
====

METAR (METeorological Aerodrome Reports) telegrams are automated weather observations for the aeronautics community that are issued by aeronautics authorities worldwide. They adhere to a very specific format, which you can read about here_ (in the present case, we are using the NOAA US format - please keep in mind other METAR formats might be slightly different!). Your mission, should you choose to accept it, is to edit the ``MetarDecoder`` object in ``src/decoder.py`` (and *none other*!) to parse METAR telegrams.

The telegrams need to be parsed into a dict suitable for encoding as an Avro_ object. The schema of the Avro object is in ``src/schema.py`` as the ``metar`` dict. You can see the fields, and their formats, listed under the ``fields`` key. This should indicate to you what the keys in your output dict ought to be and what format their values ought to be in. It also shows which keys need to be extracted from the METAR telegram (we are not interested in anything not in the schema). At this point, it may be worthwhile to check out the Avro documentation on schemata_. In particular, keep in mind the ``map`` encoding of layers aloft (you might find this referred to as 'cloud cover' in other contexts). Layers aloft should be encoded as ``altitude: type``. For instance, the layers aloft part of the following METAR message

    ``KORD 051551Z 05015KT 6SM -RA BR FEW007 BKN023 OVC029 06/04 A2978 RMK AO2 PRESFR SLP088 P0008 T00610044 $``


should be parsed as

.. code-block:: python

    {"layers_aloft":
        {"007": "FEW",
         "023": "BKN",
         "029": "OVC}
    }


Also make sure you submit values in the right format - integers vs floats etc.


Guidelines
==========

Some guidelines:

* All code is to be written for Python 3.5. If you have any dependencies beyond those in the ``requirements.txt`` file, they should be added to the requirements file.
* Code must comply with ``PEP8`` unless otherwise warranted.
* All classes and public class methods must be properly documented.
* Acceptable documentation formats are PEP287_, NumPy_ and Google_. Either is fine, but please be consistent.
* You can omit documenting types if you annotate them inline (PEP3107_ and PEP484_).
* Type annotation (PEP526_) is not expected, but is always nice to have.
* Your code *must* pass type checking (see PEP484_).
* Indent using 4 spaces.

Keep in mind that your solution must be scalable. The METARs enclosed are relatively small, but your solution must be able to handle millions of METARs. Think about what the most economic way of structuring such a solution is, not what shows off your skills best. There are many ways (``pyparsing``, regexes, ``ANTLR4``,... to name a few!) to solve this problem, and none are uniquely right or wrong. However, make sure your solution is not overkill.

There is no error handling built in, so you must cater for some way to log parsing errors, deal with them using sensible default values (by convention, in aeronautics, ``999`` and ``9999`` are used in lieu of ``N/A``) and make sure that the show goes on.


Submission
==========

Fork this repo, then make your changes. Once you're done, e-mail me a link to your repository (make sure you let me know which branch you made the changes onto!).

Before submission, I strongly suggest testing the parser-encoder on the included METAR files in the ``examples/`` folder. Using the ``fastavro`` CLI, you can dump and pretty-print an Avro file as JSON. This lets you inspect the results of your encoding and should tell you if anything has gone pear-shaped.

Good luck!

.. _PEP526: https://www.python.org/dev/peps/pep-0526/
.. _PEP484: https://www.python.org/dev/peps/pep-0484/
.. _PEP3107: https://www.python.org/dev/peps/pep-3107/
.. _Google: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
.. _NumPy: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
.. _PEP287: https://www.python.org/dev/peps/pep-0287/
.. _here: http://www.nws.noaa.gov/om/aviation/res/METAR-TAF%20Card.doc
.. _Avro: https://avro.apache.org
.. _schemata: https://avro.apache.org/docs/current/spec.html#schemas

