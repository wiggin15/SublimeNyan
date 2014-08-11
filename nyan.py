import sublime, sublime_plugin

FRAMES = u"\u1351\u1354\u1363\u1365\u1368\u1369"
RAINBOW = u'\u136b'
OUTERSPACE = u"\u1375"
NYAN_SIZE = 40

class NyanListener(sublime_plugin.EventListener):
    def __init__(self):
        from itertools import cycle
        super(NyanListener, self).__init__()
        self.frames = cycle(FRAMES)

    def on_selection_modified(self, view):
        pos = float(view.sel()[-1].end()) / float(view.size())
        num_bullets = min(NYAN_SIZE - 1, int(NYAN_SIZE * pos))
        s = RAINBOW * num_bullets + next(self.frames) + OUTERSPACE * max(0, (NYAN_SIZE - num_bullets - 1))
        view.set_status('anyan', s)
