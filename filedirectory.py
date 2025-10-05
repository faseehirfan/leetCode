from typing import Dict, Optional, List, Tuple, Union

class Node:
    def __init__(self, name: str, parent: Optional["Directory"] = None):
        self.name = name
        self.parent = parent

    def path(self) -> str:
        parts = []
        node = self
        while node is not None and node.name != "":
            parts.append(node.name)
            node = node.parent
        return "/" + "/".join(reversed(parts))


class File(Node):
    def __init__(self, name: str, parent: Optional["Directory"] = None, content: str = ""):
        super().__init__(name, parent)
        self.content = content


class Directory(Node):
    def __init__(self, name: str, parent: Optional["Directory"] = None):
        super().__init__(name, parent)
        self.children: Dict[str, Node] = {}

    def add_child(self, node: Node):
        if node.name in self.children:
            raise FileExistsError(f"Node '{node.name}' already exists in {self.path()}")
        self.children[node.name] = node
        node.parent = self

    def get_child(self, name: str) -> Optional[Node]:
        return self.children.get(name)

    def remove_child(self, name: str):
        if name in self.children:
            del self.children[name]
        else:
            raise FileNotFoundError(f"No such child: {name}")


class FileSystem:
    def __init__(self):
        self.root = Directory(name="", parent=None)
        self.cwd = self.root

    def _split_path(self, path: str) -> Tuple[bool, List[str]]:
        if path == "":
            return False, []
        is_abs = path.startswith("/")
        parts = [p for p in path.split("/") if p not in ("", ".")]
        return is_abs, parts

    def _resolve(self, path: str, create_missing=False) -> Node:
        is_abs, parts = self._split_path(path)
        node: Node = self.root if is_abs else self.cwd

        for i, part in enumerate(parts):
            if part == "..":
                node = node.parent if node.parent is not None else self.root
                continue

            if isinstance(node, File):
                raise NotADirectoryError(f"'{node.path()}' is not a directory")

            child = node.get_child(part)  # type: ignore
            if child is None:
                if create_missing:
                    new_dir = Directory(name=part, parent=node)
                    node.children[part] = new_dir  # type: ignore
                    node = new_dir
                else:
                    raise FileNotFoundError(
                        f"No such file or directory: {part} "
                        f"(in {'/' if is_abs else ''}{'/'.join(parts[:i])})"
                    )
            else:
                node = child
        return node

    def pwd(self) -> str:
        return self.cwd.path()

    def ls(self, path: Optional[str] = None) -> List[str]:
        target = self.cwd if path is None or path == "" else self._resolve(path)
        if isinstance(target, File):
            return [target.name]
        return sorted(target.children.keys())

    def mkdir(self, path: str, parents: bool = True):
        is_abs, parts = self._split_path(path)
        if not parts:
            return
        parent_parts, final_name = parts[:-1], parts[-1]

        node = self.root if is_abs else self.cwd
        for part in parent_parts:
            if part == "..":
                node = node.parent if node.parent is not None else self.root
                continue
            child = node.get_child(part)  # type: ignore
            if child is None:
                if parents:
                    new_dir = Directory(name=part, parent=node)
                    node.children[part] = new_dir  # type: ignore
                    node = new_dir
                else:
                    raise FileNotFoundError(f"Parent directory '{part}' does not exist")
            else:
                if isinstance(child, File):
                    raise NotADirectoryError(f"'{child.path()}' is a file")
                node = child

        if final_name not in ("", "."):
            existing = node.get_child(final_name)
            if existing is None:
                new_dir = Directory(name=final_name, parent=node)
                node.children[final_name] = new_dir  # type: ignore
            elif isinstance(existing, File):
                raise FileExistsError(f"File exists with name '{final_name}'")

    def touch(self, path: str):
        is_abs, parts = self._split_path(path)
        if not parts:
            raise ValueError("touch requires a filename")
        parent_parts, filename = parts[:-1], parts[-1]

        node = self.root if is_abs else self.cwd
        for part in parent_parts:
            if part == "..":
                node = node.parent if node.parent is not None else self.root
                continue
            child = node.get_child(part)  # type: ignore
            if child is None:
                new_dir = Directory(name=part, parent=node)
                node.children[part] = new_dir  # type: ignore
                node = new_dir
            else:
                if isinstance(child, File):
                    raise NotADirectoryError(f"'{child.path()}' is a file")
                node = child

        existing = node.get_child(filename)
        if existing is None:
            new_file = File(name=filename, parent=node, content="")
            node.children[filename] = new_file  # type: ignore
        elif isinstance(existing, Directory):
            raise IsADirectoryError(f"'{existing.path()}' is a directory")

    def cd(self, path: str):
        if path == "" or path == ".":
            return
        target = self._resolve(path)
        if isinstance(target, File):
            raise NotADirectoryError(f"'{target.path()}' is not a directory")
        self.cwd = target

    def write(self, path: str, data: str):
        is_abs, parts = self._split_path(path)
        if not parts:
            raise ValueError("write requires a filename")
        parent_part, filename = "/".join(parts[:-1]), parts[-1]
        if parent_part != "":
            self.mkdir(("/" if is_abs else "") + parent_part, parents=True)
        self.touch(("/" if is_abs else "") + "/".join(parts))
        node = self._resolve(("/" if is_abs else "") + "/".join(parts))
        if isinstance(node, Directory):
            raise IsADirectoryError(f"'{node.path()}' is a directory")
        node.content = data  # type: ignore

    def read(self, path: str) -> str:
        node = self._resolve(path)
        if isinstance(node, Directory):
            raise IsADirectoryError(f"'{node.path()}' is a directory")
        return node.content  # type: ignore

    def echo(self, text: str, path: str, append: bool = False):
        """Like echo in a shell: write or append text to file."""
        self.touch(path)
        node = self._resolve(path)
        if isinstance(node, Directory):
            raise IsADirectoryError(f"'{node.path()}' is a directory")
        if append:
            node.content += text
        else:
            node.content = text


fs = FileSystem()

fs.mkdir("/docs")
fs.cd("/docs")
fs.echo("hello\n", "file.txt")
print(fs.read("file.txt"))    # hello\n

fs.echo("world\n", "file.txt", append=True)
print(fs.read("file.txt"))    # hello\nworld\n

fs.cd("..")
print(fs.ls())
