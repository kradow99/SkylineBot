# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\7")
        buf.write("\n\66\n\n\f\n\16\n9\13\n\3\13\5\13<\n\13\3\f\6\f?\n\f")
        buf.write("\r\f\16\f@\3\r\3\r\3\16\3\16\3\17\3\17\3\20\6\20J\n\20")
        buf.write("\r\20\16\20K\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2")
        buf.write("\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2R\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\3!\3\2\2\2\5$\3\2\2\2\7&\3\2\2\2\t(")
        buf.write("\3\2\2\2\13*\3\2\2\2\r,\3\2\2\2\17.\3\2\2\2\21\60\3\2")
        buf.write("\2\2\23\62\3\2\2\2\25;\3\2\2\2\27>\3\2\2\2\31B\3\2\2\2")
        buf.write("\33D\3\2\2\2\35F\3\2\2\2\37I\3\2\2\2!\"\7<\2\2\"#\7?\2")
        buf.write("\2#\4\3\2\2\2$%\7*\2\2%\6\3\2\2\2&\'\7+\2\2\'\b\3\2\2")
        buf.write("\2()\7]\2\2)\n\3\2\2\2*+\7_\2\2+\f\3\2\2\2,-\7}\2\2-\16")
        buf.write("\3\2\2\2./\7\177\2\2/\20\3\2\2\2\60\61\7.\2\2\61\22\3")
        buf.write("\2\2\2\62\67\5\25\13\2\63\66\5\25\13\2\64\66\5\27\f\2")
        buf.write("\65\63\3\2\2\2\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2")
        buf.write("\678\3\2\2\28\24\3\2\2\29\67\3\2\2\2:<\t\2\2\2;:\3\2\2")
        buf.write("\2<\26\3\2\2\2=?\t\3\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2")
        buf.write("@A\3\2\2\2A\30\3\2\2\2BC\7-\2\2C\32\3\2\2\2DE\7/\2\2E")
        buf.write("\34\3\2\2\2FG\7,\2\2G\36\3\2\2\2HJ\t\4\2\2IH\3\2\2\2J")
        buf.write("K\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\b\20\2\2N \3")
        buf.write("\2\2\2\b\2\65\67;@K\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IS = 1
    LPAR = 2
    RPAR = 3
    LSQUA = 4
    RSQUA = 5
    LCURL = 6
    RCURL = 7
    COMMA = 8
    ID = 9
    CHAR = 10
    NUM = 11
    ADD = 12
    RES = 13
    MUL = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'+'", 
            "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "IS", "LPAR", "RPAR", "LSQUA", "RSQUA", "LCURL", "RCURL", "COMMA", 
            "ID", "CHAR", "NUM", "ADD", "RES", "MUL", "WS" ]

    ruleNames = [ "IS", "LPAR", "RPAR", "LSQUA", "RSQUA", "LCURL", "RCURL", 
                  "COMMA", "ID", "CHAR", "NUM", "ADD", "RES", "MUL", "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


