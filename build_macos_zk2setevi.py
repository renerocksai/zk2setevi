from cx_Freeze import setup,Executable


includes = ["atexit", "libzk2setevi",
            "pygments",
            "pygments",
            "pygments.formatters._mapping",
            "pygments.formatters.bbcode",
            "pygments.formatters.html",
            "pygments.formatters.img",
            "pygments.formatters.irc",
            "pygments.formatters.latex",
            "pygments.formatters.other",
            "pygments.formatters.rtf",
            "pygments.formatters.svg",
            "pygments.formatters.terminal",
            "pygments.formatters.terminal256",
            "pygments.lexers._asy_builtins",
            "pygments.lexers._cl_builtins",
            "pygments.lexers._cocoa_builtins",
            "pygments.lexers._csound_builtins",
            "pygments.lexers._lasso_builtins",
            "pygments.lexers._lua_builtins",
            "pygments.lexers._mapping",
            "pygments.lexers._mql_builtins",
            "pygments.lexers._openedge_builtins",
            "pygments.lexers._php_builtins",
            "pygments.lexers._postgres_builtins",
            "pygments.lexers._scilab_builtins",
            "pygments.lexers._sourcemod_builtins",
            "pygments.lexers._stan_builtins",
            "pygments.lexers._stata_builtins",
            "pygments.lexers._tsql_builtins",
            "pygments.lexers._vim_builtins",
            "pygments.lexers.actionscript",
            "pygments.lexers.agile",
            "pygments.lexers.algebra",
            "pygments.lexers.ambient",
            "pygments.lexers.ampl",
            "pygments.lexers.apl",
            "pygments.lexers.archetype",
            "pygments.lexers.asm",
            "pygments.lexers.automation",
            "pygments.lexers.basic",
            "pygments.lexers.bibtex",
            "pygments.lexers.business",
            "pygments.lexers.c_cpp",
            "pygments.lexers.c_like",
            "pygments.lexers.capnproto",
            "pygments.lexers.chapel",
            "pygments.lexers.clean",
            "pygments.lexers.compiled",
            "pygments.lexers.configs",
            "pygments.lexers.console",
            "pygments.lexers.crystal",
            "pygments.lexers.csound",
            "pygments.lexers.css",
            "pygments.lexers.d",
            "pygments.lexers.dalvik",
            "pygments.lexers.data",
            "pygments.lexers.diff",
            "pygments.lexers.dotnet",
            "pygments.lexers.dsls",
            "pygments.lexers.dylan",
            "pygments.lexers.ecl",
            "pygments.lexers.eiffel",
            "pygments.lexers.elm",
            "pygments.lexers.erlang",
            "pygments.lexers.esoteric",
            "pygments.lexers.ezhil",
            "pygments.lexers.factor",
            "pygments.lexers.fantom",
            "pygments.lexers.felix",
            "pygments.lexers.forth",
            "pygments.lexers.fortran",
            "pygments.lexers.foxpro",
            "pygments.lexers.functional",
            "pygments.lexers.go",
            "pygments.lexers.grammar_notation",
            "pygments.lexers.graph",
            "pygments.lexers.graphics",
            "pygments.lexers.haskell",
            "pygments.lexers.haxe",
            "pygments.lexers.hdl",
            "pygments.lexers.hexdump",
            "pygments.lexers.html",
            "pygments.lexers.idl",
            "pygments.lexers.igor",
            "pygments.lexers.inferno",
            "pygments.lexers.installers",
            "pygments.lexers.int_fiction",
            "pygments.lexers.iolang",
            "pygments.lexers.j",
            "pygments.lexers.javascript",
            "pygments.lexers.julia",
            "pygments.lexers.jvm",
            "pygments.lexers.lisp",
            "pygments.lexers.make",
            "pygments.lexers.markup",
            "pygments.lexers.math",
            "pygments.lexers.matlab",
            "pygments.lexers.ml",
            "pygments.lexers.modeling",
            "pygments.lexers.modula2",
            "pygments.lexers.monte",
            "pygments.lexers.ncl",
            "pygments.lexers.nimrod",
            "pygments.lexers.nit",
            "pygments.lexers.nix",
            "pygments.lexers.oberon",
            "pygments.lexers.objective",
            "pygments.lexers.ooc",
            "pygments.lexers.other",
            "pygments.lexers.parasail",
            "pygments.lexers.parsers",
            "pygments.lexers.pascal",
            "pygments.lexers.pawn",
            "pygments.lexers.perl",
            "pygments.lexers.php",
            "pygments.lexers.praat",
            "pygments.lexers.prolog",
            "pygments.lexers.python.py",
            "pygments.lexers.qvt",
            "pygments.lexers.r",
            "pygments.lexers.rdf",
            "pygments.lexers.rebol",
            "pygments.lexers.resource",
            "pygments.lexers.rnc",
            "pygments.lexers.roboconf",
            "pygments.lexers.robotframework",
            "pygments.lexers.ruby",
            "pygments.lexers.rust",
            "pygments.lexers.sas",
            "pygments.lexers.scripting",
            "pygments.lexers.shell",
            "pygments.lexers.smalltalk",
            "pygments.lexers.smv",
            "pygments.lexers.snobol",
            "pygments.lexers.special",
            "pygments.lexers.sql",
            "pygments.lexers.stata",
            "pygments.lexers.supercollider",
            "pygments.lexers.tcl",
            "pygments.lexers.templates",
            "pygments.lexers.testing",
            "pygments.lexers.text",
            "pygments.lexers.textedit",
            "pygments.lexers.textfmts",
            "pygments.lexers.theorem",
            "pygments.lexers.trafficscript",
            "pygments.lexers.typoscript",
            "pygments.lexers.urbi",
            "pygments.lexers.varnish",
            "pygments.lexers.verification",
            "pygments.lexers.web",
            "pygments.lexers.webmisc",
            "pygments.lexers.whiley",
            "pygments.lexers.x10",
            "pygments.styles.abap",
            "pygments.styles.algol",
            "pygments.styles.algol_nu",
            "pygments.styles.arduino",
            "pygments.styles.autumn",
            "pygments.styles.borland",
            "pygments.styles.bw",
            "pygments.styles.colorful",
            "pygments.styles.default",
            "pygments.styles.emacs",
            "pygments.styles.friendly",
            "pygments.styles.fruity",
            "pygments.styles.igor",
            "pygments.styles.lovelace",
            "pygments.styles.manni",
            "pygments.styles.monokai",
            "pygments.styles.murphy",
            "pygments.styles.native",
            "pygments.styles.paraiso_dark",
            "pygments.styles.paraiso_light",
            "pygments.styles.pastie",
            "pygments.styles.perldoc",
            "pygments.styles.rainbow_dash",
            "pygments.styles.rrt",
            "pygments.styles.sas",
            "pygments.styles.stata",
            "pygments.styles.tango",
            "pygments.styles.trac",
            "pygments.styles.vim",
            "pygments.styles.vs",
            "pygments.styles.xcode",
]
includefiles = [('data/setevi-template.html', 'data/setevi-template.html')]  #path_platforms
excludes = [
    '_gtkagg', '_tkagg', 'bsddb', 'curses', 'pywin.debugger',
    'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
    'Tkconstants', 'Tkinter', 'scipy', "numpy", "numpy.core"
]
packages = ["os", ]
path = []

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
                     "includes":      includes,
                     "include_files": includefiles,
                     "excludes":      excludes,
                     "packages":      packages,
                     "path":          path
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
exe = None


zk2setevi = Executable(
      script="zk2setevi.py",
      initScript = None,
    )

semantic_zk = Executable(
      script="semantic_zk.py",
      initScript = None,
)


setup(
      name = "zk2setevi",
      version = "0.1",
      author = 'Rene Schallner',
      description = "Convert Zettelkasten to Setevi",
      options = {"build_exe": build_exe_options},
      executables = [zk2setevi, semantic_zk]
)
