from js import document
from pyodide import create_proxy

function_proxy = create_proxy(runPython)

print ("hello")
