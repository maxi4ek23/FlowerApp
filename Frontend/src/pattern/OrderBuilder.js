class Order {
    constructor(price, deliveryType, clientId, bouquets) {
        this.price = price;
        this.deliveryType = deliveryType;
        this.clientId = clientId;
        this.bouquets = bouquets;
    }
}

export class OrderBuilder {
    constructor() {
        this.reset();
    }

    reset() {
        this.price = 0;
        this.deliveryType = '';
        this.clientId = 0;
        this.bouquets = [];
    }

    setPrice(price) {
        this.price = price;
        return this;
    }

    setDeliveryType(deliveryType) {
        this.deliveryType = deliveryType;
        return this;
    }

    setClientId(clientId) {
        this.clientId = clientId;
        return this;
    }

    setBouquets(bouquetData) {
        bouquetData.forEach(bouquetItem => {
            const { item, count } = bouquetItem;
            for (let i = 0; i < count; i++) {
                this.bouquets.push(item);
            }
        });
        return this;
    }

    build() {
        const order = new Order(this.price, this.deliveryType, this.clientId, this.bouquets);
        this.reset();
        return order;
    }
}