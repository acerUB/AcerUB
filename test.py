from pyrogram import Client
import threading
from datetime import datetime

# Ваши данные API
api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone_number = 'your_phone_number'

# Создаем клиента Pyrogram
app = Client("my_bot", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

# Глобальные переменные для хранения текущего ника и био
current_nickname = "DefaultNickname"
current_bio = "Default Bio"

# Функция для изменения ника и био
def change_info():
    global current_nickname, current_bio
    
    # Получаем текущее время
    current_time = datetime.now().strftime("%H:%M")
    
    # Генерируем новый никнейм и био
    new_nickname = f"NewNickname_{current_time}"
    new_bio = f"Привет // Время: {current_time}"
    
    # Меняем никнейм
    app.update_profile(username=new_nickname)
    current_nickname = new_nickname
    
    # Меняем био
    app.update_profile(bio=new_bio)
    current_bio = new_bio
    
    threading.Timer(60, change_info).start()

# Запускаем бота
if __name__ == "__main__":
    threading.Timer(60, change_info).start()
    app.run()
