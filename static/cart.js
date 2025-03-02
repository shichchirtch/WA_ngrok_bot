// Находим форму по ID и добавляем обработчик события "submit" (отправка формы)

document.getElementById("orderForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Останавливаем стандартную отправку формы, чтобы обработать данные вручную

    // Получаем значения полей ввода
    const address = document.getElementById("address").value;
    const phone = document.getElementById("phone").value;
    const payment = document.getElementById("payment").value;
    const BASE_URL = "https://f1af-2a00-20-8-1dfb-c3-5496-c60c-67b1.ngrok-free.app";


    // Валидация адреса:
    // 1. Он не должен состоять только из цифр (должна быть хотя бы одна буква).
    // 2. Длина должна быть минимум 10 символов.
    if (!/\D/.test(address) || address.length < 10) {
        alert("Адрес должен содержать хотя бы одну букву и быть не короче 10 символов.");
        return; // Прекращаем выполнение, если адрес не соответствует требованиям
    }

    // Валидация телефона:
    // 1. Должны быть только цифры и знак "+", никаких других символов.
    // 2. Длина номера должна быть от 12 до 14 символов.
    if (!/^\+?\d{12,14}$/.test(phone)) {
        alert("Телефон должен содержать только цифры и знак +, длиной от 12 до 14 символов.");
        return; // Прекращаем выполнение, если номер не соответствует требованиям
    }

    // Отправляем данные заказа на сервер с помощью fetch API
    fetch(`/cart`, {
        method: "POST", // HTTP-метод запроса
        headers: { "Content-Type": "application/json" }, // Указываем, что отправляем JSON
        body: JSON.stringify({ address, phone, payment }) // Преобразуем объект в JSON-строку
    })
    .then(response => response.json()) // Преобразуем ответ сервера в JSON
    .then(data => {
        if (data.success) { // Если сервер ответил, что заказ успешно создан
            alert("Заказ успешно оформлен!");
            window.location.href = "/"; // Перенаправляем пользователя на главную страницу
        } else { // Если произошла ошибка на сервере
            alert("Ошибка: " + data.error);
        }
    })
    .catch(error => {
        alert("Ошибка сети при отправке заказа!"); // Выводим сообщение в случае сетевой ошибки
    });
});


document.getElementById("resetOrder").addEventListener("click", function(event) {
    event.preventDefault(); // Отменяем стандартный переход по ссылке

    fetch(`/reset-cart`, { method: "POST" }) // Отправляем запрос на сервер для очистки корзины
        .then(response => response.json()) // Преобразуем ответ в JSON
        .then(data => {
            if (data.success) {
                window.location.href = "/"; // Перенаправляем пользователя на главную страницу
            } else {
                alert("Ошибка при очистке корзины!");
            }
        })
        .catch(error => {
            alert("Ошибка сети при очистке корзины!");
        });
});




