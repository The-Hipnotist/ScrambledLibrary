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
    masstrans = translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(text, dest="af").text, dest="ht").text, dest="ha").text, dest="haw").text, dest="iw").text, dest="hi").text, dest="hmn").text, dest="hu").text, dest="is").text, dest="ig").text, dest="id").text, dest="ga").text, dest="it").text, dest="ja").text, dest="jw").text, dest="en").text
    done = True
    scrambled_text = masstrans
    if output_to_file:
        with open('doubleyolk_output.txt', 'w') as f:
            f.write(scrambled_text)
    return scrambled_text