#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################################
# AUTHOR: [emraheren]
# DATE: 2021-04-20
# DESCRIPTION: Kobo Aura H2O e-book reader highleted notes exporter
######################################################################

# Copyright (C) 2021
# Emrah Eren <emrah.eren@outlook.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.#

import sys
import getopt
from src.KoboDBConnector import KoboDBConnector
from src.OutputGenerator import OutputGenerator


def main(argv):
    # Main
    if argv.__len__() == 0:
        print("Try 'KoboNoteExporter --help' for more information.")
    else:
        inputFile = None
        txtOutput = None
        csvOutput = None
        findBook = None

        try:
            opts, args = getopt.getopt(argv, "h:i:f:t:c:", ["input=", "txt=", "find=", "csv="])
            for opt, arg in opts:
                if opt == "-h":
                    usage()
                    sys.exit()
                elif opt in ("-i", "--input"):
                    inputFile = arg
                elif opt in ("-f", "--find"):
                    findBook = arg
                elif opt in ("-t", "--txt"):
                    txtOutput = arg
                elif opt in ("-c", "--csv"):
                    csvOutput = arg

            dbCon = KoboDBConnector(inputFile)

            if findBook is not None:
                liste = dbCon.getData(findBook)
            else:
                liste = dbCon.getAllData()

            if liste is None or "":
                print("Can't retrieve data!")
            else:
                output = OutputGenerator(liste)

                if txtOutput is not None:
                    output.saveAsTxt(txtOutput)

                if csvOutput is not None:
                    output.saveAsCsv(csvOutput)

        except getopt.GetoptError:
            usage()
            sys.exit(2)


def usage():
    # usage of parameters explained
    print("Arguments for usage:")
    print(" -h, --help: Help for usage")
    print(" -i, --input: Path to KoboReader.sqlite file")
    print(" -f, --find: Find Book")
    print(" -t, --txt: Text output file")
    print(" -c, --csv: CSV output file\n")
    print("Examples:\n")

    print("-Export all highlights as txt file:")
    # print ("KoboNoteExporter.py -i <input file> -t <output file>")
    print("KoboNoteExporter.py -i KoboReader.sqlite -t Output.txt\n")

    print("-Export searched book as txt file:")
    # print ("KoboNoteExporter.py -i <input file> -f <find Book> -t <output file>")
    print("KoboNoteExporter.py -i KoboReader.sqlite f 'Hamlet' -t Output.txt\n")

    print("-Export all highlights as csv file:")
    # print ("KoboNoteExporter.py -i <input file> -c <output file>")
    print("KoboNoteExporter.py -i KoboReader.sqlite -c Output.csv\n")

    print("-Export earched book as csv file:")
    # print ("KoboNoteExporter.py -i <input file> -f <find Book> -c <output file>")
    print("KoboNoteExporter.py -i KoboReader.sqlite -f 'Hamlet' -c Output.csv\n")


if __name__ == "__main__":
    main(sys.argv[1:])
