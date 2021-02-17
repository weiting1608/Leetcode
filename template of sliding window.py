# start & end of sliding window
# Focus on two pointers

def slidingWindow(self, seq):
    start, end = 0, 0
    while end < len(seq):
        # end pointer grows in the outer loop
        end += 1

        # start pointer grows with some restrict
        while self.startCondition(start):
            # process logic before pointers movement
            self.process_logic1(start, end)
            # start grows in the inner loop
            start += 1

        # or process logica after pointers movement
        self.process_logic2(start, end)

