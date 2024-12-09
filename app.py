from flask import Flask
from app.routes import create_routes
from app.models import init_db

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

init_db()  # Initialize database (e.g., in-memory or file-based for simplicity)
create_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
