from textx import metamodel_from_file

mog_meta = metamodel_from_file('mog_abstract_syntax.tx')
mog_model = mog_meta.model_from_file('test.mog')

