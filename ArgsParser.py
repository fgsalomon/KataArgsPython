__author__ = 'fgsalomon'


class ArgsParser:

    def __init__(self, schema, args):
        self.schema = schema
        self.args = args
        self.parsedArgs = {}
        self.argsCorrect = True

    def get(self, key):
        return self.parsedArgs[key]

    def parse(self):
        for key, value in self.schema.items():
            if key in self.args:
                try:
                    arg_value = self.args[self.args.index(key)+1]
                    if arg_value in self.schema:
                        self.parsedArgs[key] = value
                    else:
                        if isinstance(value, bool):
                            self.parsedArgs[key] = (arg_value == 'True')
                        elif isinstance(value, list):
                            self.parsedArgs[key] = arg_value.split(',')
                        else:
                            try:
                                self.parsedArgs[key] = type(value)(arg_value)
                            except ValueError:
                                print("Wrong type for argument: ", key,
                                      " Expected type is: ", type(value),
                                      " Using default value: ", value)
                                self.parsedArgs[key] = value
                                self.argsCorrect = False
                except IndexError:
                    self.parsedArgs[key] = value
            else:
                self.parsedArgs[key] = value
                self.argsCorrect = False
        return self.argsCorrect
