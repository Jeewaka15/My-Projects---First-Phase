from flask import Flask, request, jsonify
import os

from hash_identifier import identify_hash, save_result

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("hash-identifier.html")


@app.route('/api/identify', methods=['POST'])
def api_identify():
    data = request.get_json()
    if not data or 'hash' not in data:
        return jsonify({'error': 'hash field required'}), 400

    h = data['hash']
    results = identify_hash(h)

    out = []
    for algo, confidence, mode in results:
        line = f"{h} | {algo} | {confidence} | Mode {mode}"
        save_result(line)
        out.append({'algorithm': algo, 'confidence': confidence, 'mode': mode})

    return jsonify({'hash': h, 'results': out})


@app.route('/api/scan', methods=['POST'])
def api_scan():
    data = request.get_json() or {}
    filename = data.get('filename', 'hashes.txt')

    if not os.path.exists(filename):
        return jsonify({'error': 'file not found'}), 404

    out = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            hv = line.strip()
            if not hv:
                continue
            results = identify_hash(hv)
            for algo, confidence, mode in results:
                save_result(f"{hv} | {algo} | {confidence} | Mode {mode}")
                out.append({'hash': hv, 'algorithm': algo, 'confidence': confidence, 'mode': mode})

    return jsonify({'scanned': len(out), 'results': out})


@app.route('/api/results', methods=['GET'])
def api_results():
    if not os.path.exists('results.txt'):
        return jsonify({'results': []})

    with open('results.txt', 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.strip()]

    return jsonify({'results': lines})


if __name__ == '__main__':
    app.run(debug=True, port=5500)
