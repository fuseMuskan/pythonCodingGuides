class ConfigurationManager(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.intance = super(ConfigurationManager, cls).__new__(cls)
        return cls.intance

cm = ConfigurationManager()
new_cm = ConfigurationManager()

print(cm is new_cm)
