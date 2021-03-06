__author__ = 'dwayn'


class AMSError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NoConfigFile(AMSError):
    pass

class InvalidConfigFile(AMSError):
    pass

class DependencyRequired(AMSError):
    pass

class InvalidModule(AMSError):
    pass

class InvalidValue(AMSError):
    pass