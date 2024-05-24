from http import HTTPStatus
from flask import abort

from flower_store.model.catalogue import Catalogue
from flower_store.model.bouquet import Bouquet
from flower_store.model.flower import Flower
from flower_store.model.order import Order
from flower_store.util.builder.order_builder import OrderBuilder
from flower_store.util.builder.packing_builder import PackingBuilder
from flower_store.util.observer.order_observer import OrderSubject
from flower_store.model.order import OrderObserverImpl
from flower_store import db


class OrderController:
    def __init__(self):
        self.subject = OrderSubject()

    def create_order(self, data):
        try:
            bouquet_list = []
            for bouquet_data in data.get('bouquets', []):
                bouquet_flowers = bouquet_data.get('flowers', [])
                flowers = []

                for flower_data in bouquet_flowers:
                    flower = Flower(
                        name=flower_data.get('name'),
                        color=flower_data.get('color'),
                        price=flower_data.get('price')
                    )
                    flowers.append(flower)

                bouquet_packing = bouquet_data.get('packing')
                packing_builder = PackingBuilder()
                packing = packing_builder.set_name(bouquet_packing.get('name')).set_price(
                    bouquet_packing.get('price')).build()
                catalogue = Catalogue.query.filter_by(name=bouquet_data.get('catalogue')).first()
                bouquet = Bouquet(
                    eventType=bouquet_data['eventType'],
                    price=bouquet_data['price'],
                    packing=packing,
                    catalogue=catalogue,
                    flowers=flowers
                )
                bouquet_list.append(bouquet)

            order_builder = OrderBuilder()
            order = order_builder.prepareOrder(
                price=data.get('price'),
                delivery_type=data.get('deliveryType'),
                client_id=data.get('clientId'),
                bouquets=bouquet_list
            )

            db.session.add(order)
            db.session.commit()
            new_observer = OrderObserverImpl(order.id)
            self.subject.add_observer(new_observer)
            self.subject.notify_observers(order)
            return order

        except Exception as e:
            db.session.rollback()
            raise e

    def get_order(self, id):
        order = Order.query.get(id)
        if order is None:
            abort(HTTPStatus.NOT_FOUND)
        return order

    def get_all_orders(self):
        return Order.query.all()

    def update_order(self, order_id, data):
        order = self.get_order(order_id)
        if order is None:
            abort(HTTPStatus.NOT_FOUND)

        try:
            order.price = data.get('price', order.price)
            order.deliveryType = data.get('deliveryType', order.deliveryType)
            order.clientId = data.get('clientId', order.clientId)

            bouquet_list = []
            for bouquet_data in data.get('bouquets', []):
                bouquet_flowers = bouquet_data.get('flowers', [])
                flowers = []

                for flower_data in bouquet_flowers:
                    flower = Flower(
                        name=flower_data.get('name'),
                        color=flower_data.get('color'),
                        price=flower_data.get('price')
                    )
                    flowers.append(flower)

                bouquet_packing = bouquet_data.get('packing')
                packing_builder = PackingBuilder()
                packing = packing_builder.set_name(bouquet_packing.get('name')).set_price(
                    bouquet_packing.get('price')).build()
                catalogue = Catalogue.query.filter_by(name=bouquet_data.get('catalogue')).first()
                bouquet = Bouquet(
                    eventType=bouquet_data['eventType'],
                    price=bouquet_data['price'],
                    packing=packing,
                    catalogue=catalogue,
                    flowers=flowers
                )
                bouquet_list.append(bouquet)

            order.bouquets = bouquet_list

            db.session.commit()

            observer = self.subject.find_observer(order.id)
            if observer is None:
                observer = OrderObserverImpl(order.id)
                self.subject.add_observer(observer)
            self.subject.notify_observers(order)

            return order
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_order(self, id):
        order = self.get_order(id)
        if order is None:
            abort(HTTPStatus.NOT_FOUND)

        try:
            db.session.delete(order)
            db.session.commit()
            self.subject.notify_observers(order)
            self.subject.remove_observer(order.id)
        except Exception as e:
            db.session.rollback()
            raise e
