from ast import parse, Call, walk, FunctionDef
import importlib
import inspect

from _ast import Str, Name

mod = "popen_example"
mod = importlib.import_module(mod)
p = parse(inspect.getsource(mod))

vals = []
for node in p.body:
    if isinstance(node, FunctionDef):
        for node in walk(node):
            if isinstance(node, Call):
                method_name = node.func.attr
                module_name = node.func.value.id
                if method_name == "Popen":
                    print(module_name, method_name)
                    if len(node.args) > 0:
                        for element in node.args[0].elts:
                            if isinstance(element, Str):
                                print(element.s)
                            elif isinstance(element, Name):
                                print(element.id)

