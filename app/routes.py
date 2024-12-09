from flask import jsonify, request
from app.models import Book

def create_routes(app):
    @app.route("/books", methods=["POST"])
    def create_book():
        data = request.json
        new_book = Book.create(data["title"], data["author"])
        return jsonify(new_book), 201

    @app.route("/books/<int:book_id>", methods=["GET"])
    def get_book(book_id):
        book = Book.read(book_id)
        if not book:
            return jsonify({"error": "Book not found"}), 404
        return jsonify(book)

    @app.route("/books/<int:book_id>", methods=["PUT"])
    def update_book(book_id):
        data = request.json
        updated_book = Book.update(book_id, data)
        if not updated_book:
            return jsonify({"error": "Book not found"}), 404
        return jsonify(updated_book)

    @app.route("/books/<int:book_id>", methods=["DELETE"])
    def delete_book(book_id):
        deleted_book = Book.delete(book_id)
        if not deleted_book:
            return jsonify({"error": "Book not found"}), 404
        return jsonify({"message": "Book deleted successfully"})

    @app.route("/books/search", methods=["GET"])
    def search_books():
        query = request.args.get("query", "")
        results = Book.search(query)
        return jsonify(results)

    @app.route("/books", methods=["GET"])
    def list_books():
        # Add pagination logic here if needed
        return jsonify(Book.books.values())
