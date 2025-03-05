document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ Главная страница загружена!");

    let tg = window.Telegram.WebApp;
    console.log('tg = ', tg) // Характеристики окна
    // Получаем и декодируем initData
    let initData = tg.initData || '';
    console.log("initData", initData)
    let initDataUnsafe = tg.initDataUnsafe || {};

    // Проверяем авторизацию пользователя
    if (initDataUnsafe.user) {
        console.log("User is authorized:", initDataUnsafe.user.first_name);
    } else {
        console.log("User is not authorized");
    }

    // Отправляем данные обратно боту
    document.getElementById('sendData').addEventListener('click', function() {
        tg.sendData("Some data from Mini App");
    });

    // if (window.Telegram && Telegram.WebApp) {
    //     console.log("✅ Telegram WebApp API подключен");
    //
    //     const initData = Telegram.WebApp.initDataUnsafe;
    //     console.log("📦 Данные от Telegram:", initData);
    //
    //     fetch("/receive_telegram_data", {
    //         method: "POST",
    //         headers: { "Content-Type": "application/json" },
    //         body: JSON.stringify(initData)
    //     })
    //     .then(response => response.json())
    //     .then(data => console.log("✅ Сервер ответил:", data))
    //     .catch(error => console.error("❌ Ошибка при отправке:", error));
    // } else {
    //     console.warn("⚠️ Telegram WebApp API не подключен!");
    // }



    // Логика перехода по картинкам (если нужно)
    document.querySelectorAll(".pizza-list a").forEach(link => {
        link.addEventListener("click", function (event) {
            console.log(`➡️ Переход к пицце: ${this.href}`);
        });
    });
});
