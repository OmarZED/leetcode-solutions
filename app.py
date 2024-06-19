from flask import Flask, request, render_template, jsonify
from Solution import Solution

app = Flask(__name__)
solution = Solution()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    matrix_str = request.form.get('matrix')
    matrix = eval(matrix_str)  # Unsafe, consider using safer methods
    result = solution.longestIncreasingPath(matrix)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)