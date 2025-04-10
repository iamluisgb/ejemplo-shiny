from shiny import reactive
from shiny.express import input, render, ui

ui.input_slider("x", "Slider value", min=0, max=100, value=10)

vals = reactive.value([])

# Vamos a guardar el historial de valores del slider

@reactive.effect
@reactive.event(input.x)
def _():
    vals.set([input.x()] + vals())

@render.ui
def out():
    return [ui.p(x) for x in vals()]
