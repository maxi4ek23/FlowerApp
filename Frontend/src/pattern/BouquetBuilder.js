class Bouquet {
    constructor(price, eventType, packing, flowers) {
        this.eventType = eventType;
        this.price = price;
        this.packing = packing;
        this.catalogue = {};
        this.flowers = flowers
    }
}

export class BouquetBuilder {
    constructor() {
        this.reset();
    }

    reset() {
        this.eventType = '';
        this.price = 0;
        this.packing = {};
        this.catalogue = {};
        this.flowers = [];
    }

    setEventType(eventType) {
        this.eventType = eventType;
        return this;
    }

    setPrice(price) {
        this.price = price;
        return this;
    }


    setPacking(packing) {
        this.packing = packing;
        return this;
    }

    setFlowers(flower, count) {
        for (let i = 0; i < count; i++) {
            this.flowers.push(flower);
        }
        return this;
    }

    build() {
        const bouquet = new Bouquet(this.eventType, this.price, this.packing, this.catalogue, this.flowers);
        this.reset();
        return bouquet;
    }
}