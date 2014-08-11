import sublime, sublime_plugin

"""
0x1351 nyan-frame-1
0x1354 nyan-frame-2
0x1363 nyan-frame-3
0x1365 nyan-frame-4
0x1368 nyan-frame-5
0x1369 nyan-frame-6
0x136b rainbow
0x1375 outerspace
"""

class NyanListener(sublime_plugin.EventListener):
    def __init__(self):
        super(NyanListener, self).__init__()
        self.frame = 0

    def on_selection_modified(self, view):
        pos = float(view.sel()[-1].end()) / float(view.size())
        nyan_size = 40
        num_bullets = min(nyan_size -1, int(nyan_size * pos))
        frames = u"\u1351\u1354\u1363\u1365\u1368\u1369"
        s = u'\u136b' * num_bullets + frames[self.frame] + u"\u1375" * max(0, (nyan_size - num_bullets - 1))
        self.frame = (self.frame + 1) % len(frames)
        view.set_status('anyan', s)
