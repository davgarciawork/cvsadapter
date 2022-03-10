import os
import types
import pandas as pd
from inspect import getmembers, isfunction


def run(file):
    outputfile = output_filepath(file)
    adapt_csv(pd.read_csv(file)).to_csv(outputfile, index=False)
    return outputfile


def output_filepath(file):
    file_ext = os.path.splitext(file)
    return file_ext[0] + "_output" + file_ext[1]


def adapt_csv(csvfile):
    rules = mapping_rules_mod()
    apply_rules(getmembers(rules, isfunction), csvfile)
    return apply_mappings(rules, csvfile)


def mapping_rules_mod():
    return importCode(rules_src_code(), "rules")


def rules_src_code():
    filepath = "mapping_rules.py"
    code = ""
    with open(filepath) as infile:
        code = infile.read()
    return code


def importCode(code, name):
    module = types.ModuleType(name)
    exec(code, module.__dict__)
    return module


def apply_rules(mod_functions, csvfile):
    for mod_function in mod_functions:
        # rule_func is tuple("func_name","function")
        csvfile = apply_rule(csvfile, mod_function)


def apply_mappings(rules, csvfile):
    csvfile = csvfile[rules.mappings.keys()]
    return csvfile.rename(columns=rules.mappings)


def apply_rule(csvfile, mod_function):
    func_name = mod_function[0]
    rule_func = mod_function[1]
    # create column and add to dataframe
    csvfile[func_name] = csvfile.apply(lambda row: rule_func(row), axis=1)

    return csvfile

    # filename = input("Enter the metadata filepath to convert:")
    # output_file_message = "Enter output filepath (default is '" + output_default + ")':"
    # outputfile = input(output_file_message)
    # if not outputfile:
    #    outputfile = output_default
    # print(outputfile)
    # csvfile.to_csv(outputfile, index=False)
