import threading
from GDI_effects.GDI import Effects
#

def run_effect(effect):
    try:
        effect()
    except Exception as e:
        print(f"Ошибка в {effect.__name__}: {e}")


threads = [
    threading.Thread(target=run_effect, args=(Effects.bw_screen,)),
    threading.Thread(target=run_effect, args=(Effects.copy_screen,)),

    threading.Thread(target=run_effect, args=(Effects.error_screen,)),
    threading.Thread(target=run_effect, args=(Effects.warning_screen,)),
    threading.Thread(target=run_effect, args=(Effects.question_screen,)),
    threading.Thread(target=run_effect, args=(Effects.asterisk_screen,)),
    threading.Thread(target=run_effect, args=(Effects.super_icon_screen,)),

    threading.Thread(target=run_effect, args=(Effects.invert_screen,)),
    threading.Thread(target=run_effect, args=(Effects.pan_screen,)),
    threading.Thread(target=run_effect, args=(Effects.rainbow_blink,)),
    threading.Thread(target=run_effect, args=(Effects.screen_wavy,)),
    threading.Thread(target=run_effect, args=(Effects.void_screen,)),
    threading.Thread(target=run_effect, args=(Effects.glitch_screen,)),
    threading.Thread(target=run_effect, args=(Effects.tunnel_screen,)),
    threading.Thread(target=run_effect, args=(Effects.twisted_screen,)),
    threading.Thread(target=run_effect, args=(Effects.rotate_screen,)),
    threading.Thread(target=run_effect, args=(Effects.repeat_block_rotation,)),
    threading.Thread(target=run_effect, args=(Effects.draw_random_scribble,)),

    threading.Thread(
        target=Effects.type_text,
        args=("Hello, world!", 100)
    ),

    threading.Thread(target=run_effect, args=(Effects.flip_screen_upside_down,)),
]


for thread in threads:
    thread.daemon = True
    thread.start()


for thread in threads:
    thread.join()
