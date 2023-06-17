import pytest



def test_create_size_for_order_service(create_size_for_order):
    size = create_size_for_order.json
    pytest.assume(create_size_for_order.status.startswith('200'))
    pytest.assume(size['_id'])
    pytest.assume(size['name'])
    pytest.assume(size['price'])



def test_get_sizes_sizes_for_order_service(client, create_sizes_for_orders, 
                                           size_for_order_uri):
    response = client.get(size_for_order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_sizes_sizes_for_order = {size_for_order['_id']: size_for_order 
                                      for size_for_order in response.json}
    for size in create_sizes_for_orders:
        pytest.assume(size['_id'] in returned_sizes_sizes_for_order)
