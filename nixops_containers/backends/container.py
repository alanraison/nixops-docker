from nixops.backends import MachineDefinition, MachineState

class ContainerDefinition(MachineDefinition):
    """Definition of a container"""
    
    @classmethod
    def get_type(cls):
        return "container"