from mycroft import MycroftSkill, intent_file_handler


class Talking(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('talking.intent')
    def handle_talking(self, message):
        self.speak_dialog('talking')


def create_skill():
    return Talking()

