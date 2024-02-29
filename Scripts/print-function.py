# @author dilldylanpickle
# @category GhidraScripts

# Will print out a decompiled main function

# @keybinding
# @menupath GhidraScripts.Will print out a decompiled main function

from ghidra.app.decompiler import DecompInterface, DecompileOptions
from ghidra.util.task import ConsoleTaskMonitor

# Retrieve the currently active program within Ghidra's environment.
program = getCurrentProgram()
interface = DecompInterface()
interface.openProgram(program)

# Get the exact decompiler shown in the window
options = DecompileOptions()
interface.setOptions(options)

# Get the main function
function = getGlobalFunctions('main')[0]

# Decompile the function and print the pseudo C
results = interface.decompileFunction(function, 0, ConsoleTaskMonitor())
print(results.getDecompiledFunction().getC())