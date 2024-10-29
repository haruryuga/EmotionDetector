from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector  # Import the emotion detector function

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze.", 400

    # Call the emotion_detector function with the provided text
    response = emotion_detector(text_to_analyze)
    
    # Extract emotions and the dominant emotion from the response
    anger = response.get('anger', None)
    disgust = response.get('disgust', None)
    fear = response.get('fear', None)
    joy = response.get('joy', None)
    sadness = response.get('sadness', None)
    dominant_emotion = response.get('dominant_emotion', None)

    # Check if the dominant emotion is None (indicating invalid text or input)
    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400

    # Format the response string as per the customer’s requirements
    result_string = (
        f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return result_string

@app.route("/")
def render_index_page():
    """Render the index page of the application.

    Returns:
        str: Rendered HTML page for the index.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
