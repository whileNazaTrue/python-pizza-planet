from app.plugins import ma
from .models import (Ingredient, Size, Order, Beverage,
Customer, Report, IngredientForOrder, BeverageForOrder, SizeForOrder)


class IngredientSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')


class IngredientForOrderSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = IngredientForOrder
        load_instance = True
        fields = ('_id', 'name', 'price')


class BeverageSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price')


class BeverageForOrderSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BeverageForOrder
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeForOrderSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SizeForOrder
        load_instance = True
        fields = ('_id', 'name', 'price')


class CustomerSerializer(ma.SQLAlchemyAutoSchema):
    orders = ma.Nested('OrderSerializer', many=True, exclude=('customer',))

    class Meta:
        model = Customer
        load_instance = True
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'orders'
        )


class OrderSerializer(ma.SQLAlchemyAutoSchema):
    #size = ma.Nested(SizeSerializer)
    ingredients = ma.Nested(IngredientSerializer, many=True)
    beverages = ma.Nested(BeverageSerializer, many=True)
    customer = ma.Nested(CustomerSerializer, exclude=('orders',))
    ingredients_for_order = ma.Nested(IngredientForOrderSerializer, many=True)
    beverages_for_order = ma.Nested(BeverageForOrderSerializer, many=True)
    size_for_order = ma.Nested(SizeForOrderSerializer)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'date',
            # 'size',
            'total_price',
            'ingredients_for_order',
            'customer',
            'beverages_for_order',
            'size_for_order'
        )


class ReportSerializer(ma.SQLAlchemyAutoSchema):
    most_requested_ingredient = ma.Nested(IngredientSerializer)
    top_customers = ma.Nested(
        CustomerSerializer, many=True, exclude=('orders',))

    class Meta:
        model = Report
        load_instance = True
        fields = (
            '_id',
            'most_requested_ingredient',
            'year',
            'month_with_most_revenue',
            'sales_in_month_with_most_revenue',
            'top_customers',
            'created_at'
        )
