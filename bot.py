from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from skyline import *
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.SkylineVisitor import SkylineVisitor
import pickle
import os


def evalMsg(msg, t):
    input_stream = InputStream(msg)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    visitor = SkylineVisitor(t)
    tree = parser.root()
    result = visitor.visit(tree)
    return result


def start(update, context):
    context.user_data.clear()
    username = update.effective_chat.first_name
    message = "SkylineBot!\nBenvingut %s" % username
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def help(update, context):
    msg = '*Manual d’us del SkylineBot* 🤖\n\
    Aquest bot genera skylines graficats a partir de les instruccións que rep, i els mostra amb una imatge.\n\
    Les possibles instruccións són:\n\
    *Unió* => skyline+skyline\n\
    *Intersecció* => skyline\*skyline\n\
    *Replicació N vegades* => skyline\*N\n\
    *Despl. dreta N posicions* => skyline+N\n\
    *Despl. esquerra N posicions* => skyline-N\n\
    *Reflectir skyline* => -skyline\n\
    (S’admet l’ús de parèntesis)\n\
    Un skyline es pot definir com:\n\
    *Simple* => (xmin,alçada,xmax)\n\
    *Compost* => [(xmin,alçada,xmax)...]\n\
    *Aleatori* => {n,h,w,xmin,xmax}, que construeix n edificis, cadascun d’ells amb una alçada aleatòria entre 0 i h, amb una amplada aleatòria entre 1 i w, i una posició d’inici i de final aleatòria entre xmin i xmax.\n\
    Es poden assignar *identificadors* als skylines => a:=(1,5,3)\n\
    Les comandes del bot són:\n\
    /start inicia la conversa amb el Bot.\n\
    /help mostra manual del bot.\n\
    /author mostra nom i email de l’autor.\n\
    /lst mostra els identificadors definits i la seva àrea.\n\
    /clean esborra tots els identificadors definits.\n\
    /save id: guarda un skyline definit amb el nom id.sky.\n\
    /load id: carrega un skyline de l’arxiu id.sky.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode='Markdown')


def author(update, context):
    try:
        message = "Marcos Gómez Vázquez\nmarcos.gomez.vazquez@est.fib.upc.edu"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text='💣')


def lst(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Identificadors de Skylines definits i la seva àrea:')
    msg = ""
    for k in context.user_data:
        msg += (k + " => " + str(context.user_data[k].area) + "\n")
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


def clean(update, context):
    context.user_data.clear()
    context.bot.send_message(chat_id=update.effective_chat.id, text="S'han esborrat tots els identificadors de Skylines")


def save(update, context):
    try:
        if len(context.args) != 1:
            context.bot.send_message(chat_id=update.effective_chat.id, text="❌ ERROR\nIntrodueix un únic paràmetre que sigui un identificador definit!")
        else:
            id = context.args[0]
            skyline = context.user_data[id]
            path = os.getcwd() + '/chat_' + str(update.effective_chat.id)
            name = path + '/' + id + ".sky"
            if not os.path.isdir(path):
                os.mkdir(path)
            pickle.dump(skyline, open(name, "wb"))
            context.bot.send_message(chat_id=update.effective_chat.id, text="S'ha guardat el Skyline \'" + id + "\'")

    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣 No existeix el Skyline \'' + context.args[0] + '\'')


def load(update, context):
    try:
        if len(context.args) != 1:
            context.bot.send_message(chat_id=update.effective_chat.id, text="❌ ERROR\nIntrodueix un únic paràmetre que sigui un identificador prèviament guardat!")
        else:
            id = context.args[0]
            path = os.getcwd() + '/chat_' + str(update.effective_chat.id) + '/' + id + ".sky"
            skyline = pickle.load(open(path, "rb"))
            context.user_data[id] = skyline
            context.bot.send_message(chat_id=update.effective_chat.id, text="S'ha carregat el Skyline \'" + id + "\'")
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣 No existeix el Skyline \'' + context.args[0] + '\'')


def getText(update, context):
    if update.message.text[0] != '/':
        result = evalMsg(update.message.text, context.user_data)
        if result is not None:
            if result.id is not None:
                context.user_data[result.id] = result
            p = Skyline.getPlot(result.buildings)
            p.savefig("plot")
            p.clf()
            a = result.area
            h = result.height
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('plot.png', 'rb'))
            msg = "area: " + str(a) + "\n" + "alçada: " + str(h)
            context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
            os.remove('plot.png')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='💣')

TOKEN = '1136273985:AAGW1Wwu746b0yPm9a777mXqaog_9szWPec'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))

dispatcher.add_handler(MessageHandler(Filters.text, getText))


updater.start_polling()
