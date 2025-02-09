class Modification:
    new: str
    old: str
    change_type: str

    def __init__(self, data: str):
        pass


class Diff:
    path: str
    changes: list[Modification]
    lang: str
    full: str

    def __init__(self, data: str):
        # print("data: \n", data)
        data = self._parse_path(data)
        # print("data2: \n", data)
        # print("p: \n", self.path)
        self.full = data
        pass

    def _parse_path(self, data: str) -> str:
        paths, data = data.lstrip().split("\n", 1)
        self.path = "./" + paths.split()[1].split("/", 1)[1]
        return data

    def __repr__(self) -> str:
        r = ""
        r += "changes in file" + self.path + "\n"
        r += self.full
        return r


def parse_diff(file: str) -> list[Diff]:
    # TODO read into buffer to allow handling of larger files
    diffs = []
    with open(file, "r") as f:
        for block in f.read().split("diff --git")[1:]:
            diffs.append(Diff(block))

    return diffs
