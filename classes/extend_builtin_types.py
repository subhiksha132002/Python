class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.upper())
print(text.duplicate())


class TrackableList(list):
    def append(self, value):
        print("Append checking")
        super().append(value)


l = TrackableList()
l.append(1)
