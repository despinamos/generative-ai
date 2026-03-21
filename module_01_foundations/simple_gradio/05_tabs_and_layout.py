import gradio as gr

# Tab 1 functions
def celcius_to_fahrenheit(c: float) -> str:
    f = (c * 9/5) + 32
    return f"The temp {c} in Celcius is **{f:.1f}** in Fahrenheit"

def fahrenheit_to_celcius(f: float) -> str:
    c = (f - 32) * 5/9
    return f"The temp {f} in Fahrenheit is **{c:.1f}** in Celcius"

# Tab 2 functions
def calculate_bmi(weight: float, height: float) -> str:
    if height <= 0:
        return "Enter a valid height"
    bmi = weight / (height / 100) ** 2

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return f"### BMI: {bmi:.1f}\n **Category:** {category}"

# Tab 3 functions
def count_words(text: str) -> str:
    if not text.strip():
        return "Type some text above"
    words = len(text.split())
    chars = len(text)
    lines = len(text.splitlines())
 
    return f"**{words}** words | **{chars}** chars | **{lines}** lines"

with gr.Blocks(title="Multi-Tool App") as demo:
    gr.Markdown("# Multi-Tool App")
    gr.Markdown("An app with **tabs** and **layout**")

    with gr.Tabs():
        #Tab 1: Temperature comverter
        with gr.TabItem("Temperature"):
            gr.Markdown("### Convert Temperatures")

            with gr.Row():
                with gr.Column():
                    c_input = gr.Number(label="Celcius", value=0)
                    c_btn = gr.Button("Convert to F", variant="primary")
                    c_result = gr.Markdown()
                
                with gr.Column():
                    f_input = gr.Number(label="Fahreinheit", value=32)
                    f_btn = gr.Button("Convert to C", variant="primary")
                    f_result = gr.Markdown()
            
            c_btn.click(celcius_to_fahrenheit, c_input, c_result)
            f_btn.click(fahrenheit_to_celcius, f_input, f_result)

        # Tab 2: BMI Calculator
        with gr.TabItem("BMI"):
            gr.Markdown("### Calculate your Body Mass Index")

            with gr.Row():
                weight = gr.Number(label="Weight (kg)", value=0)
                height = gr.Number(label="Height (cm)", value=0)

            bmi_btn = gr.Button("Calculate BMI", variant="primary")
            bmi_result = gr.Markdown()
            
            bmi_btn.click(calculate_bmi, [weight, height], bmi_result)

        # Tab 3: Word counter
        with gr.TabItem("Word Counter"):
            gr.Markdown("### Count words, characters and lines in given text")

            text_input = gr.Textbox(
                label="Your text",
                placeholder="Paste or type some text here..",
                lines=5
            )

            word_result = gr.Markdown()

            # live=True

            word_result = gr.Markdown()
            
            text_input.change(count_words, text_input, word_result)
 
if __name__ == "__main__":
    demo.launch()