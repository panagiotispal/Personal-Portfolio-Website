from flask import Flask, render_template
import mysql.connector  # <--- ΔΙΟΡΘΩΣΗ 1: Η σωστή βιβλιοθήκη

app = Flask(__name__)

# Ρυθμίσεις σύνδεσης (Πρόσθεσα και το database name που έλειπε)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'amritpal',  # Ο κωδικός σου όπως φαίνεται στην εικόνα
    'database': 'portfolio_db' # <--- ΔΙΟΡΘΩΣΗ 2: Πρέπει να ξέρει ποια βάση να ανοίξει
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) # <--- ΔΙΟΡΘΩΣΗ 3: cursor αντί για corsor
    
    cursor.execute('SELECT * FROM projects')
    projects_data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('index.html', projects=projects_data)

if __name__ == '__main__':
    app.run(debug=True)