from flask import Flask, render_template, request
from src.pipeline.preediction_pipeline import PredictionPipeline, CustomeClass

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def prediction_data():
    if request.method == "GET":
        # Ensure your attractive HTML is named home.html
        return render_template("home.html")
    
    else:
        try:
            # Capturing data from the form
            # request.form.get handles missing values more gracefully
            data = CustomeClass(
                age = int(request.form.get("age", 0)),
                workclass = int(request.form.get("workclass", 0)),
                education_num = int(request.form.get("education_num", 0)),
                marital_status = int(request.form.get("marital_status", 0)),
                occupation = int(request.form.get("occupation", 0)),
                relationship = int(request.form.get("relationship", 0)),
                race = int(request.form.get("race", 0)),
                sex = int(request.form.get("sex", 0)),
                # Adding default values for fields not in your simple UI but required by model
                capital_gain = int(request.form.get("capital_gain", 0)),
                capital_loss = int(request.form.get("capital_loss", 0)),
                hours_per_week = int(request.form.get("hours_per_week", 40)),
                native_country = int(request.form.get("native_country", 38))
            )

            # Convert to DataFrame and Predict
            final_data = data.get_data_DataFrame()
            pipeline_prediction = PredictionPipeline()
            pred = pipeline_prediction.predict(final_data)

            # Income classification logic
            if pred == 0:
                res_text = "Your Yearly Income is Less than or Equal to 50k"
            else:
                res_text = "Your Yearly Income is More than 50k"

            return render_template("results.html", final_result=res_text)

        except Exception as e:
            return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    # debug=True development ke waqt use karein taaki changes turant dikhein
    app.run(host="0.0.0.0", port=7860, debug=True)
