#!/usr/bin/python
#UTF-8
__author__ = 'gulliver - Radek Simkanic - SIM0094'

import sys
import messages as msg


class Argument:
    def __init__(self, short, long, description, contains_value = True, required = False):
        if isinstance(short, str) == False or isinstance(long, str) == False or isinstance(description, str) == False:
            msg.message(
                msg.SYSTEM_ERROR,
                "Parameters short, long and description must be string",
                TypeError
            )
        if isinstance(contains_value, bool) == False:
            msg.message(
                msg.SYSTEM_ERROR,
                "Parameter contains_value must be bool",
                TypeError
            )
        if isinstance(required, bool) == False:
            msg.message(
                msg.SYSTEM_ERROR,
                "Parameter required must be bool",
                TypeError
            )
        if len(short) == 0 and len(long) == 0:
            msg.message(
                msg.SYSTEM_ERROR,
                "At least one of the parameters (short, long) must be filled",
                ValueError
            )

        self.short = short
        self.long = long
        self.description = description
        self.contains_value = contains_value
        self.required = required
        self.function_name_check_value = ""
        self.function_name = ""
        self.params = []
        self.value = ""
        self.is_correct = True
        self.is_selected = False
        self.is_all_dependencies = True
        self.nothing_incompatible = True
        self.dependencies = []
        self.incompatible = []
        self.all_arguments = []
        self.what_is_incompatible = None

    # @rewrite
    def _check(self, value):
        return True

    def isSelected(self):
        return self.is_selected

    def isCorrect(self):
        return self.is_selected and self.is_correct and self.is_all_dependencies and self.nothing_incompatible

    def getValue(self):
        return self.value


    def setDependencies(self, list_of_arguments):
        if not isinstance(list_of_arguments, list):
            msg.message(
                msg.SYSTEM_ERROR,
                "list_of_arguments must be list",
                TypeError
            )
        self.dependencies = list_of_arguments
        return self

    def setIncompatibleArguments(self, list_of_arguments):
        if not isinstance(list_of_arguments, list):
            msg.message(
                msg.SYSTEM_ERROR,
                "list_of_arguments must be list",
                TypeError
            )
        self.incompatible = list_of_arguments
        return self


    def _checkDependencies(self):
        for d in self.dependencies:
            if isinstance(d, list): # sublist is OR for each item
                found = False
                for d2 in d:
                    if d2 in self.all_arguments:
                        found = True
                        break
                if not found:
                    self.is_all_dependencies = False
                    self.what_need = " OR ".join(map(str,d))
                    return False
                continue
            if d not in self.all_arguments:
                self.is_all_dependencies = False
                self.what_need = d
                return False
        return True

    def _checkIncompatible(self):
        for i in self.incompatible:
            if i in self.all_arguments:
                self.nothing_incompatible = False
                self.what_is_incompatible = i
                return False
        return True

    def _getWhatIsIncompatible(self):
        return self.what_is_incompatible

    def _getWhatNeedArgument(self):
        return self.what_need

    def _getShort(self):
        return self.short

    def _getLong(self):
        return self.long

    def _getDescription(self):
        return self.description

    def _containsValue(self):
        return self.contains_value

    def _setValue(self, value):
        r = self._check(value)
        if r is True or (r is tuple and r[0] is True):
            self.value = value
            return True
        return r

    def _setSelected(self):
        self.is_selected = True

    def _setAllArguments(self, list_of_arguments):
        self.all_arguments = list_of_arguments

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "argument (short: %s%s, long: %s%s)"%(Arguments.short_prefix, self.short, Arguments.long_prefix, self.long)

# And example how to create own argument checker
class ExampleArgument:
    pass


class Arguments:
    short_prefix = "-"
    long_prefix = "--"
    last_clear_command = "s"

    head_information = "List of possible arguments."
    shadow_argument = None
    allowed_empty_arguments = False

    arguments = []
    arguments_for_checking = {}
    used_arguments = []

    execution_arguments = []

    def __init__(self):
        self.ready = False

        if len(sys.argv) <= 1:
            self.is_empty = True

        else:
            self.execution_arguments = sys.argv[1:]
            self.is_empty = False

        self.help_argument = Argument(
            "h", "help", "This help information", False
        )

        self.addArgument(self.help_argument)

    ### BEGIN SETTERS ###
    def setHeadInformation(self, information):
        self.head_information = information
        return self

    def setShortPrefix(self, prefix):
        self.short_prefix = prefix
        return self

    def setLongPrefix(self, prefix):
        self.long_prefix = prefix
        return self

    def allowedEmptyArguments(self, allowed = True):
        self.allowed_empty_arguments = allowed

        if not allowed and self.is_empty:
            msg.message(msg.ERROR, "You must set any arguments (for help -h)")

        return self

    ### END SETTERS ###

    def isEmpty(self):
        return self.is_empty_arguments

    def addArgument(self, argument, is_shaddow_argument = False):
        if self.ready:
            msg.message(
                msg.SYSTEM_ERROR,
                "After calling method check is not possible call method addArgument",
                StandardError
            )
        if isinstance(argument, Argument):
            if len(argument._getShort()):
                self.arguments_for_checking[str(self.short_prefix) + argument._getShort()] = argument
            if len(argument._getLong()):
                self.arguments_for_checking[str(self.long_prefix) + argument._getLong()] = argument

            argument._setAllArguments(self.used_arguments)
            self.arguments.append(argument)

            if is_shaddow_argument:
                self.shadow_argument = argument

            return self
        else:
            msg.message(
                msg.SYSTEM_ERROR,
                "Type must be instance of Argument, not %s"%type(argument),
                TypeError
            )

    def check(self):
        if self.ready:
            msg.message(
                msg.SYSTEM_ERROR,
                "After calling method check is not possible call method check",
                StandardError
            )
        self.ready = True

        if self.is_empty:
            if not self.allowed_empty_arguments:
                msg.message(msg.ERROR, "You must set any arguments (for help -h)")
            return self

        again_continue = False
        set_value = None
        last_argument = self.execution_arguments[-1]
        for a in self.execution_arguments:
            if again_continue:
                again_continue = False
                continue

            if set_value is not None:
                r = set_value._setValue(a)
                r_e = r # error
                r_m = "" # message
                if isinstance(r, tuple):
                    r_e = bool(r[0])
                    r_m = "\nMessage: %s"%str(r[1])

                if r_e is False:
                    p = []
                    if len(set_value._getShort()):
                        p.append(self.short_prefix + set_value._getShort())
                    if len(set_value._getLong()):
                        p.append(self.long_prefix + set_value._getLong())
                    msg.message(
                        msg.ERROR,
                        "%s can't accept this value: %s%s"%(set_value, a, r_m)
                    )
                set_value = None
                continue

            if self.arguments_for_checking.has_key(a):
                a_obj = self.arguments_for_checking[a]
                if a_obj in self.used_arguments:
                    if a_obj._containsValue():
                        again_continue = True
                    continue
                a_obj._setSelected()
                self.used_arguments.append(a_obj)
                if a_obj._containsValue():
                    set_value = a_obj
            elif a == last_argument:
                self.shadow_argument._setValue(a)

        if self.help_argument in self.used_arguments:
            self.__help()

        self.__checkDependencies()
        self.__checkIncompatible()
        return self

    def __checkDependencies(self):
        for a in self.used_arguments:
            if not a._checkDependencies():
                msg.message(
                    msg.ERROR,
                    "Is not set all dependencies: %s\n\t is needed: %s"%(a, a._getWhatNeedArgument())
                )

    def __checkIncompatible(self):
        for a in self.used_arguments:
            if not a._checkIncompatible():
                msg.message(
                    msg.ERROR,
                    "Incompatible arguments between: \n\t%s \n\t%s"%(str(a), str(a._getWhatIsIncompatible()) )
                )

    def __help(self):
        template = "\t%s%s%s\t%s"

        print "HELP"

        print self.head_information

        if len(self.arguments):
            print "\nShort commands:"
            for a in self.arguments:
                if len(a._getShort()):
                    v = ""
                    if a._containsValue():
                        v = " [value]"

                    print template % (self.short_prefix, a._getShort(), v, a._getDescription())

            print "\nLong commands:"
            for a in self.arguments:
                if len(a._getLong()):
                    v = ""
                    if a._containsValue():
                        v = " [value]"

                    print template % (self.long_prefix, a._getLong(), v, a._getDescription())
        sys.exit()
