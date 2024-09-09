from googletrans import Translator
import threading, time, itertools, sys, os
translator = Translator()

def scramble(text, output_to_file=False):
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write("\rScrambling..." + c)
            sys.stdout.flush()
            time.sleep(0.1)
        os.system("cls")
    t = threading.Thread(target=animate)
    t.start()
    masstrans = translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(text, dest="af").text, dest="ht").text, dest="ha").text, dest="haw").text, dest="iw").text, dest="hi").text, dest="hmn").text, dest="hu").text, dest="is").text, dest="ig").text, dest="id").text, dest="ga").text, dest="it").text, dest="ja").text, dest="jw").text, dest="kn").text, dest="kk").text, dest="km").text, dest="ko").text, dest="ku").text, dest="ky").text, dest="lo").text, dest="la").text, dest="lv").text, dest="lt").text, dest="lb").text, dest="mk").text, dest="mg").text, dest="ms").text, dest="ml").text, dest="mt").text, dest="mi").text, dest="mr").text, dest="mn").text, dest="my").text, dest="ne").text, dest="no").text, dest="or").text, dest="ps").text, dest="fa").text, dest="pl").text, dest="pl").text, dest="pt").text, dest="pa").text, dest="pa").text, dest="ro").text, dest="ru").text, dest="sm").text, dest="gd").text, dest="sr").text, dest="st").text, dest="sn").text, dest="sd").text, dest="si").text, dest="sk").text, dest="sl").text, dest="so").text, dest="es").text, dest="su").text, dest="sw").text, dest="sv").text, dest="tg").text, dest="ta").text, dest="te").text, dest="th").text, dest="tr").text, dest="uk").text, dest="ur").text, dest="uz").text, dest="vi").text, dest="cy").text, dest="xh").text, dest="yi").text, dest="yo").text, dest="en").text
    done = True
    scrambled_text = masstrans
    if output_to_file:
        with open('deviled_output.txt', 'w') as f:
            f.write(scrambled_text)
    return scrambled_text