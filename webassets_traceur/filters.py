from webassets.filter import Filter
from subprocess import check_call


class TraceurFilter(Filter):

    name = "traceur"
    max_debug_level = None

    def setup(self):
        def _get(name, default):
            return self.get_config(name, require=False) or default

        self._bin = _get('TRACEUR_BIN', 'traceur')
        self._experimental = _get("TRACEUR_EXPERIMENTAL", False)

    def unique(self):
        return id(self)

    def output(self, _in, out, **kwargs):
        out.write(_in.read())

    def input(self, _in, out, **kwargs):

        args = [self._bin, "--out", kwargs["output_path"]]
        if self._experimental:
            args.append("--experimental")

        args.append("--script")
        args.append(kwargs["source_path"])

        check_call(args)

        # HACK: flask-script must work in memory pipes
        with open(kwargs["output_path"], "rb") as stream:
            out.write(stream.read().decode())
