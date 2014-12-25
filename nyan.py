import sublime, sublime_plugin

FRAMES = u"\u1AB2\u1AB3\u1AB4\u1AB5\u1AB6\u1AB7"
FRAMES_TBG = u"\u1ABA\u1ABB\u1ABC\u1ABD\u1ABE\u1ABF"
RAINBOW = u'\u1AB8'
RAINBOW_TBG = u'\u1AC0'
OUTERSPACE = u"\u1AB9"
OUTERSPACE_TBG = u"\u1AC1"
NYAN_SIZE = 40

class NyanListener(sublime_plugin.EventListener):
    def __init__(self):
        from itertools import cycle
        import platform, os
        super(NyanListener, self).__init__()
        self.tbg = sublime.load_settings("Nyan.sublime-settings").get("transparent-background", False)
        self.frames = cycle(FRAMES_TBG if self.tbg else FRAMES)
        self.enabled = platform.system() == "Darwin" and os.path.exists(os.path.expanduser("~/Library/Fonts/Nyan.ttf"))
        #self.enabled = False

    def on_selection_modified(self, view):
        if view.size() == 0 or not self.enabled:
            return
        pos = float(view.sel()[-1].end()) / float(view.size())
        num_bullets = min(NYAN_SIZE - 1, int(NYAN_SIZE * pos))
        rainbow = RAINBOW_TBG if self.tbg else RAINBOW
        outerspace = OUTERSPACE_TBG if self.tbg else OUTERSPACE
        s = rainbow * num_bullets + next(self.frames) + outerspace * max(0, (NYAN_SIZE - num_bullets - 1))
        view.set_status('anyan', s)
