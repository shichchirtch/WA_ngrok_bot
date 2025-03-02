from flask import Flask, render_template, url_for, request, redirect, jsonify
from external_functions import send_telegram_message
app = Flask(__name__)

# Список доступных пицц с их данными
pizzas = [
    {"id": 1, "name": "Маргарита", "image": "margherita.png", "description": "Томатный соус, моцарелла, базилик."},
    {"id": 2, "name": "Пепперони", "image": "pepperoni.png", "description": "Томатный соус, моцарелла, пепперони."},
    {"id": 3, "name": "Четыре сыра", "image": "four_cheese.png",
     "description": "Моцарелла, пармезан, горгонзола, эмменталь."},
    {"id": 4, "name": "Гавайская", "image": "hawaiian.png",
     "description": "Томатный соус, моцарелла, ананасы, ветчина."}]

cart = []  # Корзина для хранения выбранных пицц

@app.route("/")
def index():
    """Главная страница, отображает список всех доступных пицц."""
    return render_template("index.html", pizzas=pizzas)


@app.route("/pizza/<int:pizza_id>")
def pizza_detail(pizza_id):
    """Страница с детальной информацией о пицце."""
    pizza = next((p for p in pizzas if p["id"] == pizza_id), None)
    if pizza:
        return render_template("pizza.html", pizza=pizza)
    return "Пицца не найдена", 404  # Возвращает ошибку 404, если пицца не найдена


@app.route("/cart", methods=["GET", "POST"])
def cart_page():
    """Страница корзины. Отображает товары и обрабатывает оформление заказа."""
    if request.method == "POST":
        # Получаем данные заказа в формате JSON
        data = request.get_json()
        address = data.get("address")  #   это извлечение значения по ключу "address" из словаря data
        phone = data.get("phone")
        payment = data.get("payment")

        # Проверяем, что обязательные поля заполнены
        if not address or not phone:
            return jsonify({"success": False, "error": "Заполните все поля!"}), 400

        message = f"🛒 *Заказ оформлен!*\n" \
                  f"👤 *Заказчик:* {request.remote_addr}\n" \
                  f"📍 *Адрес:* {address}\n" \
                  f"📞 *Телефон:* {phone}\n" \
                  f"💳 *Оплата:* {payment}"

        send_telegram_message(message)

        # return jsonify({"success": True})



        # Симуляция оформления заказа (можно заменить на логику сохранения в БД)
        print(f"Заказ оформлен! Адрес: {address}, Телефон: {phone}, Оплата: {payment}")

        cart.clear()  # Очищаем корзину после оформления заказа
        return jsonify({"success": True})

    # Рассчитываем итоговую стоимость заказа
    total_price = sum(item["quantity"] * 15 for item in cart)
    return render_template("cart.html", cart=cart, total_price=total_price)


@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    """Добавляет выбранную пиццу в корзину."""
    data = request.get_json()
    pizza_id = data.get("pizza_id")
    quantity = data.get("quantity")

    if not pizza_id or quantity is None:
        return jsonify(success=False, error="Некорректные данные"), 400

    pizza = next((p for p in pizzas if p["id"] == int(pizza_id)), None)
    if pizza:
        existing_pizza = next((item for item in cart if item["pizza_id"] == pizza_id), None)
        if existing_pizza:
            existing_pizza["quantity"] += quantity  # Увеличиваем количество, если пицца уже в корзине
        else:
            cart.append({"pizza_id": pizza_id, "name": pizza["name"], "quantity": quantity})
        return jsonify(success=True)

    return jsonify(success=False, error="Пицца не найдена"), 404


@app.route("/reset-cart", methods=["POST"])
def reset_cart():
    """Очищает корзину и возвращает JSON-ответ об успешной очистке."""
    cart.clear()
    return jsonify(success=True)

