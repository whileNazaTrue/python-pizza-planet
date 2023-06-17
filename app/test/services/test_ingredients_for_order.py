import pytest



def test_create_ingredient_for_order_service(create_ingredient_for_order):
    ingredient = create_ingredient_for_order.json
    pytest.assume(create_ingredient_for_order.status.startswith('200'))
    pytest.assume(ingredient['_id'])
    pytest.assume(ingredient['name'])
    pytest.assume(ingredient['price'])



def test_get_ingredients_for_order_service(client, create_ingredients_for_order, 
                                           ingredient_for_order_uri):
    response = client.get(ingredient_for_order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_ingredients_ingredients_for_order = {ingredient_for_order['_id']: ingredient_for_order 
                                                  for ingredient_for_order in response.json}
    for ingredient in create_ingredients_for_order:
        pytest.assume(ingredient['_id'] in returned_ingredients_ingredients_for_order)
