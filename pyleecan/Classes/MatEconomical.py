# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/MatEconomical.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/MatEconomical
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError


class MatEconomical(FrozenClass):
    """material ecomomical properties"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, cost_unit=0.127, unit_name="$", init_dict=None, init_str=None):
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
            cost_unit = obj.cost_unit
            unit_name = obj.unit_name
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "cost_unit" in list(init_dict.keys()):
                cost_unit = init_dict["cost_unit"]
            if "unit_name" in list(init_dict.keys()):
                unit_name = init_dict["unit_name"]
        # Initialisation by argument
        self.parent = None
        self.cost_unit = cost_unit
        self.unit_name = unit_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MatEconomical_str = ""
        if self.parent is None:
            MatEconomical_str += "parent = None " + linesep
        else:
            MatEconomical_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        MatEconomical_str += "cost_unit = " + str(self.cost_unit) + linesep
        MatEconomical_str += 'unit_name = "' + str(self.unit_name) + '"' + linesep
        return MatEconomical_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.cost_unit != self.cost_unit:
            return False
        if other.unit_name != self.unit_name:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        MatEconomical_dict = dict()
        MatEconomical_dict["cost_unit"] = self.cost_unit
        MatEconomical_dict["unit_name"] = self.unit_name
        # The class name is added to the dict fordeserialisation purpose
        MatEconomical_dict["__class__"] = "MatEconomical"
        return MatEconomical_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.cost_unit = None
        self.unit_name = None

    def _get_cost_unit(self):
        """getter of cost_unit"""
        return self._cost_unit

    def _set_cost_unit(self, value):
        """setter of cost_unit"""
        check_var("cost_unit", value, "float", Vmin=0)
        self._cost_unit = value

    cost_unit = property(
        fget=_get_cost_unit,
        fset=_set_cost_unit,
        doc=u"""Cost of one kilo of material

        :Type: float
        :min: 0
        """,
    )

    def _get_unit_name(self):
        """getter of unit_name"""
        return self._unit_name

    def _set_unit_name(self, value):
        """setter of unit_name"""
        check_var("unit_name", value, "str")
        self._unit_name = value

    unit_name = property(
        fget=_get_unit_name,
        fset=_set_unit_name,
        doc=u"""Name of the unit

        :Type: str
        """,
    )
