#command: python setup.py build

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "os", "datetime", "fpdf", "pdf2docx", "typing", "num2words"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Manaju Docs",
    options = options,
    version = "1.0",
    description = 'None',
    executables = executables
)