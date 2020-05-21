# Generated from Skyline.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\5\2\25\n\2\3\3\3\3\5\3\31\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5*\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\7\5;\n\5\f\5\16\5>\13\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7L\n\7\f\7\16\7")
        buf.write("O\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\td\n\t\3\t\2\3\b\n\2\4")
        buf.write("\6\b\n\f\16\20\2\2\2k\2\24\3\2\2\2\4\30\3\2\2\2\6\32\3")
        buf.write("\2\2\2\b)\3\2\2\2\n?\3\2\2\2\fG\3\2\2\2\16R\3\2\2\2\20")
        buf.write("c\3\2\2\2\22\25\5\4\3\2\23\25\7\2\2\3\24\22\3\2\2\2\24")
        buf.write("\23\3\2\2\2\25\3\3\2\2\2\26\31\5\6\4\2\27\31\5\b\5\2\30")
        buf.write("\26\3\2\2\2\30\27\3\2\2\2\31\5\3\2\2\2\32\33\7\13\2\2")
        buf.write("\33\34\7\3\2\2\34\35\5\b\5\2\35\7\3\2\2\2\36\37\b\5\1")
        buf.write("\2\37 \7\4\2\2 !\5\b\5\2!\"\7\5\2\2\"*\3\2\2\2#$\7\17")
        buf.write("\2\2$*\5\b\5\f%*\7\13\2\2&*\5\n\6\2\'*\5\f\7\2(*\5\16")
        buf.write("\b\2)\36\3\2\2\2)#\3\2\2\2)%\3\2\2\2)&\3\2\2\2)\'\3\2")
        buf.write("\2\2)(\3\2\2\2*<\3\2\2\2+,\f\13\2\2,-\7\20\2\2-;\5\b\5")
        buf.write("\f./\f\t\2\2/\60\7\16\2\2\60;\5\b\5\n\61\62\f\n\2\2\62")
        buf.write("\63\7\20\2\2\63;\5\20\t\2\64\65\f\b\2\2\65\66\7\16\2\2")
        buf.write("\66;\5\20\t\2\678\f\7\2\289\7\17\2\29;\5\20\t\2:+\3\2")
        buf.write("\2\2:.\3\2\2\2:\61\3\2\2\2:\64\3\2\2\2:\67\3\2\2\2;>\3")
        buf.write("\2\2\2<:\3\2\2\2<=\3\2\2\2=\t\3\2\2\2><\3\2\2\2?@\7\4")
        buf.write("\2\2@A\5\20\t\2AB\7\n\2\2BC\5\20\t\2CD\7\n\2\2DE\5\20")
        buf.write("\t\2EF\7\5\2\2F\13\3\2\2\2GH\7\6\2\2HM\5\n\6\2IJ\7\n\2")
        buf.write("\2JL\5\n\6\2KI\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N")
        buf.write("P\3\2\2\2OM\3\2\2\2PQ\7\7\2\2Q\r\3\2\2\2RS\7\b\2\2ST\5")
        buf.write("\20\t\2TU\7\n\2\2UV\5\20\t\2VW\7\n\2\2WX\5\20\t\2XY\7")
        buf.write("\n\2\2YZ\5\20\t\2Z[\7\n\2\2[\\\5\20\t\2\\]\7\t\2\2]\17")
        buf.write("\3\2\2\2^_\7\4\2\2_`\5\20\t\2`a\7\5\2\2ad\3\2\2\2bd\7")
        buf.write("\r\2\2c^\3\2\2\2cb\3\2\2\2d\21\3\2\2\2\t\24\30):<Mc")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "IS", "LPAR", "RPAR", "LSQUA", "RSQUA", 
                      "LCURL", "RCURL", "COMMA", "ID", "CHAR", "NUM", "ADD", 
                      "RES", "MUL", "WS" ]

    RULE_root = 0
    RULE_instr = 1
    RULE_assig = 2
    RULE_sl = 3
    RULE_simple = 4
    RULE_comp = 5
    RULE_random = 6
    RULE_number = 7

    ruleNames =  [ "root", "instr", "assig", "sl", "simple", "comp", "random", 
                   "number" ]

    EOF = Token.EOF
    IS=1
    LPAR=2
    RPAR=3
    LSQUA=4
    RSQUA=5
    LCURL=6
    RCURL=7
    COMMA=8
    ID=9
    CHAR=10
    NUM=11
    ADD=12
    RES=13
    MUL=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self):
            return self.getTypedRuleContext(SkylineParser.InstrContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.LPAR, SkylineParser.LSQUA, SkylineParser.LCURL, SkylineParser.ID, SkylineParser.RES]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.instr()
                pass
            elif token in [SkylineParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(SkylineParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assig(self):
            return self.getTypedRuleContext(SkylineParser.AssigContext,0)


        def sl(self):
            return self.getTypedRuleContext(SkylineParser.SlContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_instr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = SkylineParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 20
                self.assig()
                pass

            elif la_ == 2:
                self.state = 21
                self.sl(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def IS(self):
            return self.getToken(SkylineParser.IS, 0)

        def sl(self):
            return self.getTypedRuleContext(SkylineParser.SlContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_assig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)




    def assig(self):

        localctx = SkylineParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(SkylineParser.ID)
            self.state = 25
            self.match(SkylineParser.IS)
            self.state = 26
            self.sl(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(SkylineParser.LPAR, 0)

        def sl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SlContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SlContext,i)


        def RPAR(self):
            return self.getToken(SkylineParser.RPAR, 0)

        def RES(self):
            return self.getToken(SkylineParser.RES, 0)

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def simple(self):
            return self.getTypedRuleContext(SkylineParser.SimpleContext,0)


        def comp(self):
            return self.getTypedRuleContext(SkylineParser.CompContext,0)


        def random(self):
            return self.getTypedRuleContext(SkylineParser.RandomContext,0)


        def MUL(self):
            return self.getToken(SkylineParser.MUL, 0)

        def ADD(self):
            return self.getToken(SkylineParser.ADD, 0)

        def number(self):
            return self.getTypedRuleContext(SkylineParser.NumberContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_sl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSl" ):
                return visitor.visitSl(self)
            else:
                return visitor.visitChildren(self)



    def sl(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.SlContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_sl, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 29
                self.match(SkylineParser.LPAR)
                self.state = 30
                self.sl(0)
                self.state = 31
                self.match(SkylineParser.RPAR)
                pass

            elif la_ == 2:
                self.state = 33
                self.match(SkylineParser.RES)
                self.state = 34
                self.sl(10)
                pass

            elif la_ == 3:
                self.state = 35
                self.match(SkylineParser.ID)
                pass

            elif la_ == 4:
                self.state = 36
                self.simple()
                pass

            elif la_ == 5:
                self.state = 37
                self.comp()
                pass

            elif la_ == 6:
                self.state = 38
                self.random()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 56
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.SlContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sl)
                        self.state = 41
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 42
                        self.match(SkylineParser.MUL)
                        self.state = 43
                        self.sl(10)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.SlContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sl)
                        self.state = 44
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 45
                        self.match(SkylineParser.ADD)
                        self.state = 46
                        self.sl(8)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.SlContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sl)
                        self.state = 47
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 48
                        self.match(SkylineParser.MUL)
                        self.state = 49
                        self.number()
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.SlContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sl)
                        self.state = 50
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 51
                        self.match(SkylineParser.ADD)
                        self.state = 52
                        self.number()
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.SlContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sl)
                        self.state = 53
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 54
                        self.match(SkylineParser.RES)
                        self.state = 55
                        self.number()
                        pass

             
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class SimpleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(SkylineParser.LPAR, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.NumberContext)
            else:
                return self.getTypedRuleContext(SkylineParser.NumberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMMA)
            else:
                return self.getToken(SkylineParser.COMMA, i)

        def RPAR(self):
            return self.getToken(SkylineParser.RPAR, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_simple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple" ):
                return visitor.visitSimple(self)
            else:
                return visitor.visitChildren(self)




    def simple(self):

        localctx = SkylineParser.SimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(SkylineParser.LPAR)
            self.state = 62
            self.number()
            self.state = 63
            self.match(SkylineParser.COMMA)
            self.state = 64
            self.number()
            self.state = 65
            self.match(SkylineParser.COMMA)
            self.state = 66
            self.number()
            self.state = 67
            self.match(SkylineParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQUA(self):
            return self.getToken(SkylineParser.LSQUA, 0)

        def simple(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SimpleContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SimpleContext,i)


        def RSQUA(self):
            return self.getToken(SkylineParser.RSQUA, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMMA)
            else:
                return self.getToken(SkylineParser.COMMA, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_comp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)




    def comp(self):

        localctx = SkylineParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SkylineParser.LSQUA)
            self.state = 70
            self.simple()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.COMMA:
                self.state = 71
                self.match(SkylineParser.COMMA)
                self.state = 72
                self.simple()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(SkylineParser.RSQUA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RandomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(SkylineParser.LCURL, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.NumberContext)
            else:
                return self.getTypedRuleContext(SkylineParser.NumberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMMA)
            else:
                return self.getToken(SkylineParser.COMMA, i)

        def RCURL(self):
            return self.getToken(SkylineParser.RCURL, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_random

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandom" ):
                return visitor.visitRandom(self)
            else:
                return visitor.visitChildren(self)




    def random(self):

        localctx = SkylineParser.RandomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_random)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SkylineParser.LCURL)
            self.state = 81
            self.number()
            self.state = 82
            self.match(SkylineParser.COMMA)
            self.state = 83
            self.number()
            self.state = 84
            self.match(SkylineParser.COMMA)
            self.state = 85
            self.number()
            self.state = 86
            self.match(SkylineParser.COMMA)
            self.state = 87
            self.number()
            self.state = 88
            self.match(SkylineParser.COMMA)
            self.state = 89
            self.number()
            self.state = 90
            self.match(SkylineParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(SkylineParser.LPAR, 0)

        def number(self):
            return self.getTypedRuleContext(SkylineParser.NumberContext,0)


        def RPAR(self):
            return self.getToken(SkylineParser.RPAR, 0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = SkylineParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_number)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.LPAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(SkylineParser.LPAR)
                self.state = 93
                self.number()
                self.state = 94
                self.match(SkylineParser.RPAR)
                pass
            elif token in [SkylineParser.NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(SkylineParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.sl_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def sl_sempred(self, localctx:SlContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




