from py_mini_racer import py_mini_racer

js_context = py_mini_racer.MiniRacer()
out = js_context.eval('2+3')
print(out)

processing_library = ""
with open("js/p5.js", 'r', encoding='utf-8') as p_file:
    processing_library = p_file.read()

out = js_context.eval(processing_library)
print(processing_library)
