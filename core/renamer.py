import os
from .messages import message, ERROR, WARNING, INFORMATION, DONE


class Renamer:
    def __init__(self, path):
        self.path = path if path != "" else "."
        self.first_suffix = "."
        self.second_suffix = "."
        self.files = []
        self.test_mode = False

    def testMode(self):
        self.test_mode = True

    def setFirstSuffix(self, suffix):
        self.first_suffix = suffix

    def setSecondSuffix(self, suffix):
        self.second_suffix = suffix

    def _check(self):
        if not os.path.isdir(self.path):
            message(
                ERROR,
                "Directory '%s' does not exists or is not directory"
                % self.path)

        self.files = os.listdir(self.path)

        if len(self.files) == 0:
            message(ERROR, "Directory '%s' is empty" % self.path)

        if self.path[-1] != "/":
            self.path += "/"

        if self.first_suffix == "." or self.second_suffix == ".":
            message(ERROR, "First or second suffix is bad")

        first_suffix = self.first_suffix.strip()
        second_suffix = self.second_suffix.strip()
        first_suffix = first_suffix.strip(".")
        second_suffix = second_suffix.strip(".")

        parts_first_suffix = first_suffix.split(".")
        parts_second_suffix = second_suffix.split(".")

        final_first_suffix = parts_first_suffix[-1]
        final_second_suffix = parts_second_suffix[-1]
        final_first_suffix = final_first_suffix.strip()
        final_second_suffix = final_second_suffix.strip()

        if self.first_suffix != final_first_suffix:
            message(WARNING, "First suffix is changed from '%s' to '%s'." %
                    (self.first_suffix, final_first_suffix))
            self.first_suffix = final_first_suffix
        if self.second_suffix != final_second_suffix:
            message(WARNING, "Second suffix is changed from '%s' to '%s'." %
                    (self.second_suffix, final_second_suffix))
            self.second_suffix = final_second_suffix

        if self.first_suffix == self.second_suffix:
            message(ERROR, "First and second suffix is not be same!")

        self.first_suffix = "." + self.first_suffix
        self.second_suffix = "." + self.second_suffix

        return

    def do(self):
        self._check()

        first_list = []
        second_list = []

        message(INFORMATION, "Filtering files")

        if self.test_mode:
            message(DONE, "TEST MODE ENABLED")

        for f in self.files:
            if str(f).endswith(self.first_suffix):
                first_list.append(str(f))
            elif str(f).endswith(self.second_suffix):
                second_list.append(str(f))

        if len(first_list) == 0:
            message(ERROR, "Suffix '%s' was not found!" % self.first_suffix)

        if len(second_list) == 0:
            message(ERROR, "Suffix '%s' was not found!" % self.second_suffix)

        if len(first_list) != len(second_list):
            message(
                WARNING,
                "Count: \n\tsuffix'%s': %i\n\tsuffix'%s': %i" % (
                    self.first_suffix, len(
                        first_list), self.second_suffix, len(second_list)
                )
            )

        count = len(first_list) if len(first_list) <= len(
            second_list) else len(second_list)
        first_list.sort()
        second_list.sort()

        for i in range(count):
            first_file = first_list[i]
            second_file = second_list[i]

            self._rename(first_file, second_file)

        if self.test_mode:
            message(DONE, "Test mode - DONE.")
        else:
            message(DONE, "All possible subtitle files are renamed.")

    def _rename(self, first_file, second_file):
        first_name = first_file.split(".")
        first_name = first_name[0:-1]
        first_name = ".".join(first_name)

        second_full_name = "%s%s" % (first_name, self.second_suffix)

        if not self.test_mode:
            os.renames(
                os.path.join(self.path, second_file),
                os.path.join(self.path, second_full_name)
            )

        message(INFORMATION,
                """Rename done:\n\told name: '%s' \n\tvia file: '%s'\n\tnew name: '%s'""" % (
                    second_file.encode('utf-8'), first_file.encode('utf-8'),
                    second_full_name.encode('utf-8')))
        return
