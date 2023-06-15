from app.plugins import ma
from .models import Ingredient, Size, Order, Beverage, Customer, Report


class IngredientSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class BeverageSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Beverage
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
        )


class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    ingredients = ma.Nested(IngredientSerializer, many=True)
    beverages = ma.Nested(BeverageSerializer, many=True)
    customer = ma.Nested(CustomerSerializer) 

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'date',
            'size',
            'total_price',
            'ingredients',
            'beverages',
            'customer'  
        )

class ReportSerializer(ma.SQLAlchemyAutoSchema):
    most_requested_ingredient = ma.Nested(IngredientSerializer)
    top_one_customer = ma.Nested(CustomerSerializer)
    top_two_customer = ma.Nested(CustomerSerializer)
    top_three_customer = ma.Nested(CustomerSerializer)

    class Meta:
        model = Report
        load_instance = True
        fields = (
            '_id', 
            'most_requested_ingredient', 
            'year', 
            'month_with_most_revenue',
            'sales_in_month_with_most_revenue',
            'top_one_customer',
            'top_two_customer',
            'top_three_customer',
            'created_at'
            )
        
