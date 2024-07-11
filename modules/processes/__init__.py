from .Start import StartProcess
from .StepHandler import NextStepHandler
from .Restrict import KillProcess, ShutUpProcess, UnmuteProcess

handlers_to_add = [
    NextStepHandler,

    StartProcess,
    KillProcess,
    ShutUpProcess,
    UnmuteProcess,
]