import os

# Decorator imports
from permedcoe import constraint       # To define constraints needs (e.g. number of cores)
from permedcoe import container        # To define container related needs
from permedcoe import binary           # To define binary to execute related needs
from permedcoe import mpi              # To define an mpi binary to execute related needs (can not be used with @binary)
from permedcoe import task             # To define task related needs
# @task supported types
from permedcoe import FILE_IN          # To define file type and direction
from permedcoe import FILE_OUT         # To define file type and direction
from permedcoe import FILE_INOUT       # To define file type and direction
from permedcoe import DIRECTORY_IN     # To define directory type and direction
from permedcoe import DIRECTORY_OUT    # To define directory type and direction
from permedcoe import DIRECTORY_INOUT  # To define directory type and direction
# Other permedcoe available functionalities
from permedcoe import get_environment  # Get variables from invocation (tmpdir, processes, gpus, memory)


def function_name(*args, **kwargs):
    """ Extended python interface:
    To be used only with PyCOMPSs - Enables to define a workflow within the building block.
    Tasks are not forced to be binaries: PyCOMPSs supports tasks that are pure python code.
    # PyCOMPSs help: https://pycompss.readthedocs.io/en/latest/Sections/02_App_Development/02_Python.html
    Requirement: all tasks should be executed in a container (with the same container definition)
                 to ensure that they all have the same requirements.
    """
    print("Building Block entry point to be used with PyCOMPSs")
    # TODO: (optional) Pure python code calling to PyCOMPSs tasks (that can be defined in this file or in another).


@container(engine="SINGULARITY", image="toolset.sif")
@binary(binary="Rscript --vanilla /opt/tf_enrichment.R")
@task(input_file=FILE_IN, output_file=FILE_OUT)
def tf_enrichment(input_file=None, output_file=None, verbose_flag='-v', verbose='T'):
    """
    The Definition is equal to:
        Rscript --vanilla /opt/tf_enrichment.R <de_input_file> <output_file>
    """
    pass


def invoke(input, output, config):
    print("Arguments:", input, output, config)
    tf_enrichment(input_file=input[0], output_file=output[0], verbose=input[1])
