import bimpy as bp

ctx = bp.Context()

ctx.init(600, 600, "Hello")

str = bp.String()
f = bp.Float()

while not ctx.should_close():
    with ctx:
        bp.text("Hello, world!")

        if bp.button("OK"):
            print(str.value)

        bp.input_text('string', str, 256)

        bp.slider_float("float", f, 0.0, 1.0)
