from flask import Flask, jsonify, render_template, request, make_response, Response
from predictor import predict_delay
from xhtml2pdf import pisa
from io import BytesIO
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/predict', methods=['POST'])
def predict_user_input():
    data = {
        "distance_km": float(request.form["distance_km"]),
        "vehicle_type": request.form["vehicle_type"],
        "vendor_rating": int(request.form["vendor_rating"]),
        "weather": request.form["weather"]
    }
    result = predict_delay(data)

    # Store result in session or pass directly to result.html
    return render_template("result.html",
        delay=result["predicted_delay_days"],
        reason=result["reason"],
        route_type="Fastest",
        transport_mode="Road",
        carrier_name="Blue Dart",
        weather_impact="High",
        risk_score=87,
        suggested_action="Switch to Rail mode or re-route via NH48"
    )

@app.route('/download_pdf')
def download_pdf():
    data = {
        "delay": 3,
        "reason": "Heavy rainfall along the route",
        "route_type": "Fastest",
        "transport_mode": "Road",
        "carrier_name": "Blue Dart",
        "weather_impact": "High",
        "risk_score": 87,
        "suggested_action": "Switch to Rail mode or re-route via NH48"
    }

    html = render_template("delay_prediction.html", **data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

    if not pdf.err:
        response = make_response(result.getvalue())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=shipment_prediction.pdf'
        return response
    return "PDF generation failed"

@app.route('/download_csv')
def download_csv():
    data = {
        "delay": 3,
        "reason": "Heavy rainfall along the route",
        "route_type": "Fastest",
        "transport_mode": "Road",
        "carrier_name": "Blue Dart",
        "weather_impact": "High",
        "risk_score": 87,
        "suggested_action": "Switch to Rail mode or re-route via NH48"
    }

    def generate():
        output = BytesIO()
        writer = csv.writer(output)
        writer.writerow(["Field", "Value"])
        for key, value in data.items():
            writer.writerow([key, value])
        output.seek(0)
        return output.read()

    return Response(
        generate(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=shipment_prediction.csv"}
    )

@app.route('/api/predict')
def predict_api():
    result = predict_delay()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
data = {
    "distance_km": float(request.form["distance_km"]),
    "vehicle_type": request.form["vehicle_type"],
    "vendor_rating": int(request.form["vendor_rating"]),
    "weather": request.form["weather"],
    "carrier": request.form["carrier"]   # ✅ Add this
}
result = predict_delay(data)
