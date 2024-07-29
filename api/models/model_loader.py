from . import orders, order_details, recipes, sandwiches, resources, guest_order, promotion, menu_item, guest_order

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    guest_order.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    guest_order.Base.metadata.create_all(engine)
