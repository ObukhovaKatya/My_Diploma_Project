# Екатерина Обухова, 33 когорта - Финальный проект
import sender_stand_request
import data

def test_track_order():
    # Создаём заказ и получаем трек
    create_resp = sender_stand_request.post_new_order(data.create_order_body)
    track_number = create_resp.json().get("track")

    # Получаем заказ по треку
    get_resp = sender_stand_request.get_track_order(track_number)

    # Заказ найден по треку
    assert get_resp.status_code == 200

