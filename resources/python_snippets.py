""" One line summary (end it with a period).

more detail about the module including its usage and classes. This
script provides snippet templates for modules,classes and functions
which comply with PEP257 and Google Python Style Guide 
"""

__copyright__ = "(c) Your Name 2019"
__license__ = "GNU General Public License v3"
__author__ = "your Name"
__email__ = "your.name@some.email.server.somewhere"
__version__ = "0.0.1"
__status__ = "Alpha, Beta, or Stable"

#-----------------------------------------------------------------------
# the lines below are usually put into python modules so that the main 
# function doesn't execute when the script is loaded as a module

def main():
    pass

if __name__ == '__main__':
    main()

# a class snippet that complies with PEP257 and Google docstrings
class ClassName(object):
    """ Short description.

    longer description

    Attributes:
        att1: a public attribute of the class. describe it. normally you
        don't list private attributes
    """

    def __init__(self):
        """Inits ClassName with blah."""
        pass

    def public_method(self, req_arg, opt_arg = None):
        """Short description.

        Longer description

        Args:
            req_arg: A required argument
            opt_arg: An optional argument

        Returns:
            None

        Raises:
            NoError
        """
        pass

    def _private_method(self):
        """Performs operation blah."""

        pass


# a function or method snippet that complies with PEP257 and Google
# docstrings
def function_name(req_arg, opt_arg = None):
    """Short description.

    Longer description. In this case it does nothing

    Args:
        req_arg: A required argument
        opt_arg: An optional argument

    Returns:
        None

    Raises:
        NoError
    """
    pass