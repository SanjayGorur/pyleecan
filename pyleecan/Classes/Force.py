# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Force.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Force
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Force.comp_time_angle import comp_time_angle
except ImportError as error:
    comp_time_angle = error

try:
    from ..Methods.Simulation.Force.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError


class Force(FrozenClass):
    """Forces module abstract object"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Force.comp_time_angle
    if isinstance(comp_time_angle, ImportError):
        comp_time_angle = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Force method comp_time_angle: " + str(comp_time_angle)
                )
            )
        )
    else:
        comp_time_angle = comp_time_angle
    # cf Methods.Simulation.Force.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Force method run: " + str(run))
            )
        )
    else:
        run = run
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, is_comp_nodal_force=False, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            is_comp_nodal_force = obj.is_comp_nodal_force
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "is_comp_nodal_force" in list(init_dict.keys()):
                is_comp_nodal_force = init_dict["is_comp_nodal_force"]
        # Initialisation by argument
        self.parent = None
        self.is_comp_nodal_force = is_comp_nodal_force

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Force_str = ""
        if self.parent is None:
            Force_str += "parent = None " + linesep
        else:
            Force_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Force_str += "is_comp_nodal_force = " + str(self.is_comp_nodal_force) + linesep
        return Force_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_comp_nodal_force != self.is_comp_nodal_force:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        Force_dict = dict()
        Force_dict["is_comp_nodal_force"] = self.is_comp_nodal_force
        # The class name is added to the dict fordeserialisation purpose
        Force_dict["__class__"] = "Force"
        return Force_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_comp_nodal_force = None

    def _get_is_comp_nodal_force(self):
        """getter of is_comp_nodal_force"""
        return self._is_comp_nodal_force

    def _set_is_comp_nodal_force(self, value):
        """setter of is_comp_nodal_force"""
        check_var("is_comp_nodal_force", value, "bool")
        self._is_comp_nodal_force = value

    is_comp_nodal_force = property(
        fget=_get_is_comp_nodal_force,
        fset=_set_is_comp_nodal_force,
        doc=u"""1 to compute lumped tooth forces

        :Type: bool
        """,
    )
