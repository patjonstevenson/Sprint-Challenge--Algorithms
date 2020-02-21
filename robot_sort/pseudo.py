for i in range(1, len(self._list)-1):
    self.swap_item()
    for j in range(i, len(self._list)-1):
        self.move_right()
        if self.compare_item():
            continue
        else:
            self.swap_item()
            self.
