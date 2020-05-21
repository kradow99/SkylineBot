# Generated from Skyline.g4 by ANTLR 4.7.1
from antlr4 import *
from skyline import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser


# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    def __init__(self, t={}):
        self.table = t

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx: SkylineParser.RootContext):
        return self.visit(ctx.instr())

    # Visit a parse tree produced by SkylineParser#instr.
    def visitInstr(self, ctx: SkylineParser.InstrContext):

        if (ctx.assig() is not None):
            return self.visit(ctx.assig())
        else:
            bs = self.visit(ctx.sl())
            if bs is not None:
                return Skyline(None, bs)

    # Visit a parse tree produced by SkylineParser#assig.
    def visitAssig(self, ctx: SkylineParser.AssigContext):
        id = str(ctx.ID().getText())
        sl = self.visit(ctx.sl())
        if sl is not None:
            return Skyline(id, sl)

    # Visit a parse tree produced by SkylineParser#sl.
    def visitSl(self, ctx: SkylineParser.SlContext):
        if (ctx.ID() is not None):
            try:
                return Skyline.deepcopy(self.table[ctx.ID().getText()].buildings)
            except:
                print("ID inexistent: " + ctx.ID().getText())
        elif (ctx.simple() is not None):
            return self.visit(ctx.simple())
        elif (ctx.comp() is not None):
            return self.visit(ctx.comp())
        elif (ctx.random() is not None):
            return self.visit(ctx.random())
        elif (ctx.number() is not None):
            sl1 = self.visit(ctx.sl(0))
            n = self.visit(ctx.number())
            if (ctx.MUL() is not None):
                return Skyline.replic(sl1, n)
            elif (ctx.ADD() is not None):
                return Skyline.despl(sl1, n)
            elif (ctx.RES() is not None):
                return Skyline.despl(sl1, -n)
        elif (ctx.RES() is not None):
            sl1 = self.visit(ctx.sl(0))
            return Skyline.mirror(sl1)
        elif (ctx.MUL() is not None):
            sl1 = self.visit(ctx.sl(0))
            sl2 = self.visit(ctx.sl(1))
            return Skyline.intersection(sl1, sl2)
        elif (ctx.ADD() is not None):
            sl1 = self.visit(ctx.sl(0))
            sl2 = self.visit(ctx.sl(1))
            return Skyline.union(sl1, sl2)
        else:
            return self.visit(ctx.sl(0))  # entre paréntesis

    # Visit a parse tree produced by SkylineParser#simple.
    def visitSimple(self, ctx: SkylineParser.SimpleContext):
        xmin = self.visit(ctx.number(0))
        height = self.visit(ctx.number(1))
        xmax = self.visit(ctx.number(2))
        return Skyline.simple(xmin, height, xmax)

    # Visit a parse tree produced by SkylineParser#comp.
    def visitComp(self, ctx: SkylineParser.CompContext):
        i = 0
        bs = []
        result = []
        while (ctx.simple(i) is not None):
            bs.append(self.visit(ctx.simple(i)))
            i += 1
        for b in bs:
            result = Skyline.union(result, b)
        return result

    # Visit a parse tree produced by SkylineParser#random.
    def visitRandom(self, ctx: SkylineParser.RandomContext):
        n = self.visit(ctx.number(0))
        h = self.visit(ctx.number(1))
        w = self.visit(ctx.number(2))
        xmin = self.visit(ctx.number(3))
        xmax = self.visit(ctx.number(4))
        return Skyline.random(n, h, w, xmin, xmax)

    # Visit a parse tree produced by SkylineParser#number.
    def visitNumber(self, ctx: SkylineParser.NumberContext):
        if ctx.number() is not None:
            return self.visit(ctx.number())
        else:
            return int(ctx.NUM().getText())

del SkylineParser
