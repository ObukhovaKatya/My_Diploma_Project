import sender_stand_request
import data

def test_create_order_and_get_by_track():
    # 1. Создаем заказ
    create_response = sender_stand_request.post_new_order(data.create_order_body)
    assert create_response.status_code == 201, "Заказ не создан"
    
    # 2. Получаем трек заказа
    track_number = create_response.json().get("track")
    assert track_number is not None, "Track не получен"

    # 3. Получаем заказ по треку
    get_response = sender_stand_request.get_track_order(track_number)
    assert get_response.status_code == 200, "Заказ по треку не найден"

    # 4. Проверяем данные заказа
    order_info = get_response.json().get("order")
    assert order_info["firstName"] == data.create_order_body["firstName"]
    assert order_info["lastName"] == data.create_order_body["lastName"]
    assert order_info["address"] == data.create_order_body["address"]
