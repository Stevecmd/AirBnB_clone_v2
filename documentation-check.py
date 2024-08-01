#!/usr/bin/env python3

import sys
import importlib.util
import inspect


def check_documentation(module_name):
    try:
        # Load the module
        spec = importlib.util.spec_from_file_location(
            module_name,
            module_name + ".py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Check functions and classes for documentation
        issues = []
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) or inspect.isclass(obj):
                if not obj.__doc__:
                    issues.append(f"{name} is missing documentation")

        if issues:
            print(f"{module_name}.py: Fail")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"{module_name}.py: OK")
    except Exception as e:
        print(f"Failed to check {module_name}.py: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 documentation-check.py <file1.py> <file2.py> ..")
        sys.exit(1)

    for file_path in sys.argv[1:]:
        module_name = file_path[:-3]  # Remove the .py extension
        check_documentation(module_name)
