class Person():
    def __init__(self, name, timeline, screen_name, profile_image):
        self.name = name
        self.timeline = timeline
        self.screen_name = screen_name
        self.profile_image = profile_image

    def __str__(self):
        data = {}
        data['name'] = self.name
        data['timeline'] = self.timeline
        data['screen_name'] = self.name
        data['profile_image'] = self.timeline
