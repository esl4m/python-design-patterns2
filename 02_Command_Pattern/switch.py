class Switch:
    """ The INVOKER class"""
    def __init__(self, flipUpCmd, flipDownCmd):
        self.__flipUpCommand = flipUpCmd
        self.__flipDownCommand = flipDownCmd

    def flip_up(self):
        self.__flipUpCommand.execute()

    def flip_down(self):
        self.__flipDownCommand.execute()


class Light:
    """The RECEIVER Class"""
    def turn_on(self):
        print("The light is on")

    def turn_off(self):
        print("The light is off")


class Command:
    """The Command Abstract class"""
    def __init__(self):
        pass
        #Make changes

    def execute(self):
        #OVERRIDE
        pass


class FlipUpCommand(Command):
    """The Command class for turning on the light"""
    def __init__(self,light):
        self.__light = light

    def execute(self):
        self.__light.turn_on()


class FlipDownCommand(Command):
    """The Command class for turning off the light"""
    def __init__(self,light):
        Command.__init__(self)
        self.__light = light

    def execute(self):
        self.__light.turn_off()


class LightSwitch:
    """ The Client Class"""
    def __init__(self):
        self.__lamp = Light()
        self.__switchUp = FlipUpCommand(self.__lamp)
        self.__switchDown = FlipDownCommand(self.__lamp)
        self.__switch = Switch(self.__switchUp, self.__switchDown)

    def switch(self, cmd):
        cmd = cmd.strip().upper()

        try:
            if cmd == "ON":
                self.__switch.flip_up()
            elif cmd == "OFF":
                self.__switch.flip_down()
            else:
                print("Argument \"ON\" or \"OFF\" is required.")
        except ValueError:
            print("Exception occurred")
        # except Exception, msg:
        #     print("Exception occurred: %s" % msg)

# Execute if this file is run as a script and not imported as a module
if __name__ == "__main__":
    lightSwitch = LightSwitch()

    print("Switch ON test.")
    lightSwitch.switch("ON")

    print("Switch OFF test")
    lightSwitch.switch("OFF")

    print("Invalid Command test")
    lightSwitch.switch("****")
