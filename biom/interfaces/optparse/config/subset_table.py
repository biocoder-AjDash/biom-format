#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2011-2013, The BIOM Format Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from pyqi.core.interfaces.optparse import (OptparseOption,
                                           OptparseUsageExample,
                                           OptparseResult)
from pyqi.core.command import (make_command_in_collection_lookup_f,
                               make_command_out_collection_lookup_f)
from pyqi.core.interfaces.optparse.input_handler import load_file_lines
from biom.interfaces.optparse.input_handler import biom_load_file_contents
from biom.interfaces.optparse.output_handler import write_subsetted_biom_table
from biom.commands.table_subsetter import CommandConstructor

__author__ = "Jai Ram Rideout"
__copyright__ = "Copyright 2011-2013, The BIOM Format Development Team"
__credits__ = ["Jai Ram Rideout", "Daniel McDonald",
               "Jose Antonio Navas Molina"]
__license__ = "BSD"
__url__ = "http://biom-format.org"
__maintainer__ = "Jai Ram Rideout"
__email__ = "jai.rideout@gmail.com"

cmd_in_lookup = make_command_in_collection_lookup_f(CommandConstructor)
cmd_out_lookup = make_command_out_collection_lookup_f(CommandConstructor)


usage_examples = [
    OptparseUsageExample(ShortDesc="Subsetting a json BIOM table",
                         LongDesc="Choose a subset of the observations in "
                                  "table.biom and write them to subset.biom",
                         Ex="%prog -j table.biom -a observations -s "
                            "observation_ids.txt -o subset.biom"),
    OptparseUsageExample(ShortDesc="Subsetting a hdf5 BIOM table",
                         LongDesc="Choose a subset of the observations in "
                                  "table.biom and write them to subset.biom",
                         Ex="%prog -i table.biom -a observations -s "
                            "observation_ids.txt -o subset.biom")
]

inputs = [
    OptparseOption(Parameter=cmd_in_lookup('hdf5_table'),
                   Type='existing_filepath',
                   Handler=None, ShortName='i',
                   Name='input-hdf5-fp',
                   Help='the input hdf5 BIOM table filepath to subset'),

    OptparseOption(Parameter=cmd_in_lookup('json_table_str'),
                   Type='existing_filepath',
                   Handler=biom_load_file_contents, ShortName='j',
                   Name='input-json-fp',
                   Help='the input hdf5 BIOM table filepath to subset'),

    OptparseOption(Parameter=cmd_in_lookup('axis'), ShortName='a'),

    OptparseOption(Parameter=cmd_in_lookup('ids'),
                   Type='existing_filepath', Handler=load_file_lines,
                   ShortName='s', Help='a file containing a single column of '
                   'IDs to retain (either sample IDs or observation IDs, '
                   'depending on the axis)'),

    OptparseOption(Parameter=None, Type='new_filepath', ShortName='o',
                   Name='output-fp', Required=True,
                   Help='the output BIOM table filepath'),
]

outputs = [
    OptparseResult(Parameter=cmd_out_lookup('subsetted_table'),
                   Handler=write_subsetted_biom_table,
                   InputName='output-fp')
]
