from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        print(data)
        value = data.get('value')
        # Do something with the received data (e.g., store it in a database or process it)
        print(f'Received data: {value}')
        return jsonify({'message': 'Data received successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
