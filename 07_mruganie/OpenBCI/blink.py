import numpy as np

class BlinkRealTime(object):

    def __init__(self):
        self.blinks_num = 0
        self.new_blink = False
        self.zero_crossed = True
        self.prev_val = 0.0
        self.visual = np.array([])

    def blink_detect(self, value, thr):
        self.visual = np.append(self.visual, [0.0])

        # if there is no new blink detected then this is False
        self.new_blink = False

        if value < thr and self.prev_val >= thr \
                and self.zero_crossed is True:
            if (len(self.visual) > 2):
                # blink detected at this function call
                self.new_blink = True
                self.blinks_num += 1
                self.visual[-2] = thr
                self.visual[-1] = -thr
                self.zero_crossed = False

        if self.prev_val > 0.0 and value <= 0.0:
            self.zero_crossed = True

        self.prev_val = value
