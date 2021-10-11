from pathlib import Path
from re import compile
from collections import defaultdict
from collections.abc import Iterable

from .triangle import TriangleFactory
from .face import Face
from .shape import Shape


class InvalidFileExtension(Exception):
    def __init__(self, extension, filename):
        super().__init__(
            f"File extension must be '{extension}', not {Path(filename).suffix}"
            )


class ObjectFileCharset:
    COMMENT_TAG = "#"
    VERTEX_TAG = "v"
    FACE_TAG = "f"
    FACE_ARGSEPARATOR = "/"
    ELEMENT_ARGSEPARATOR = "\t"
    ELEMENT_SEPARATOR = "\n"


class ObjectFileParser:
    ARGS_PATTERN = compile("[^\s]+")
    TAG_PATTERN = compile("[a-zA-Z]+")
    ID_PATTERN = compile("[0-9]+")

    @classmethod
    def parse_args(cls, line):
        return cls.ARGS_PATTERN.findall(line)

    @classmethod
    def parse_tag(cls, tag):
        element_tag = cls.TAG_PATTERN.search(tag)
        return element_tag.group() if element_tag != None else None

    @classmethod
    def parse_id(cls, tag):
        element_id = cls.ID_PATTERN.search(tag)
        return int(element_id.group()) if element_id != None else None

    @classmethod
    def parse_element(cls, line, tag, callback):
        args = cls.parse_args(line)
        element_tag = cls.parse_tag(args[0]) if args else None
        if element_tag != None and element_tag == tag.lower():
            return callback(args)

    @classmethod
    def parsemethod(cls, tag, callback):
        return lambda line: cls.parse_element(line, tag, callback)


class ObjectFileDecoder:
    __parsehandlers__ = (
        lambda decoder, line: ObjectFileParser.parse_element(
            line,
            ObjectFileCharset.VERTEX_TAG,
            decoder._data[ObjectFileCharset.VERTEX_TAG].append
            ),
        lambda decoder, line: ObjectFileParser.parse_element(
            line,
            ObjectFileCharset.FACE_TAG,
            lambda args: decoder._data[ObjectFileCharset.FACE_TAG].append(
                (args[0], *(arg.split(ObjectFileCharset.FACE_ARGSEPARATOR) for arg in args[1:]))
                )
            ),
        )

    def __init__(self):
        self._data = defaultdict(list)

    def decode(self, contents):
        self.reset()
        for line in contents.splitlines():
            for parser in self.__parsehandlers__:
                parser(self, line)
        return self

    def reset(self):
        self._data.clear()
        return self

    def as_triangles(self):
        triangles = []
        for element in self._data[ObjectFileCharset.FACE_TAG]:
            vertices = []
            for arg in element[1:]:
                vertex_id = ObjectFileParser.parse_id(arg[0])
                vertex = self._data[ObjectFileCharset.VERTEX_TAG][vertex_id - 1]
                vertices.append([float(i) for i in vertex[1:]])
            origin = vertices[0]
            for i, vertex in enumerate(vertices[2:]):
                triangles.append(
                    TriangleFactory.create(origin, vertices[i + 1], vertex)
                    )

        return triangles

    def as_faces(self, *args, **kwargs):
        return [
            Face(triangle, *args, **kwargs)
            for triangle in self.as_triangles()
            ]

    def as_shape(self, *args, **kwargs):
        if self._data:
            return Shape(self.as_faces(), *args, **kwargs)


class ObjectFileCompiler:
    def compile_element(tag, id, args):
        args = [
            str(arg) if isinstance(arg, str) or not isinstance(arg, Iterable) \
            else ObjectFileCharset.FACE_ARGSEPARATOR.join(str(i) for i in arg)
            for arg in args
            ]
        return ObjectFileCharset.ELEMENT_ARGSEPARATOR.join((tag, *args))


class ObjectFileEncoder:
    def __init__(self):
        self._data = defaultdict(list)

    def reset(self):
        self._data.clear()
        return self

    def compile(self):
        lines = []
        for tag, v in self._data.items():
            for i, args in enumerate(v):
                lines.append(
                    ObjectFileCompiler.compile_element(tag, i, args)
                    )
            lines.append("")
        return ObjectFileCharset.ELEMENT_SEPARATOR.join(lines)

    def add_element(self, tag, args):
        self._data[tag].append(args)
        return self

    def encode_triangles(self, triangles, *args, **kwargs):
        self.reset()
        for triangle in triangles:
            ids = []
            for vector in triangle:
                self.add_element(
                    ObjectFileCharset.VERTEX_TAG, vector
                    )
                ids.append(
                    len(self._data[ObjectFileCharset.VERTEX_TAG])
                    )
            self.add_element(
                ObjectFileCharset.FACE_TAG,
                [str(i) for i in ids]
                )
        return self.compile()

    def encode_shape(self, shape, *args, **kwargs):
        return self.encode_faces(shape.iterate_faces())

    def encode_faces(self, faces, *args, **kwargs):
        return self.encode_triangles(face.unit() for face in faces)


class ObjectFileHandler:
    OBJFILE_EXTENSION = ".obj"
    MODULE_SOURCEPATH = Path(__file__).parent.parent.joinpath("src", "obj")

    @classmethod
    def is_objfile(cls, filename):
        return Path(filename).suffix.lower() == cls.OBJFILE_EXTENSION

    @classmethod
    def source_path(cls, filename):
        return cls.MODULE_SOURCEPATH.joinpath(filename)

    @classmethod
    def read(cls, filename, *args, **kwargs):
        if cls.is_objfile(filename):
            with open(filename, "r", *args, **kwargs) as f:
                return f.read()
        else:
            raise InvalidFileExtension(cls.OBJFILE_EXTENSION, filename)

    @classmethod
    def write(cls, data, filename, *args, **kwargs):
        if cls.is_objfile(filename):
            with open(filename, "w", *args, **kwargs) as f:
                return f.write(data)
        else:
            raise InvalidFileExtension(cls.OBJFILE_EXTENSION, filename)


class ObjectFileReader:
    def read_shape(filename, *args, **kwargs):
        decoder = ObjectFileDecoder()
        decoder.decode(
            ObjectFileHandler.read(filename)
            )
        return decoder.as_shape(*args, **kwargs)

    def read_triangles(filename, *args, **kwargs):
        decoder = ObjectFileDecoder()
        decoder.decode(
            ObjectFileHandler.read(filename)
            )
        return decoder.as_triangles(*args, **kwargs)

    def read_faces(filename, *args, **kwargs):
        decoder = ObjectFileDecoder()
        decoder.decode(
            ObjectFileHandler.read(filename)
            )
        return decoder.as_faces(*args, **kwargs)


class ObjectFileWriter:
    def write_shape(shape, filename, *args, **kwargs):
        encoder = ObjectFileEncoder()
        contents = encoder.encode_shape(shape, *args, **kwargs)
        return ObjectFileHandler.write(contents, filename)

    def write_triangles(triangles, filename, *args, **kwargs):
        encoder = ObjectFileEncoder()
        contents = encoder.encode_triangles(triangles, *args, **kwargs)
        return ObjectFileHandler.write(contents, filename)

    def write_faces(faces, filename, *args, **kwargs):
        encoder = ObjectFileEncoder()
        contents = encoder.encode_faces(faces, *args, **kwargs)
        return ObjectFileHandler.write(contents, filename)
