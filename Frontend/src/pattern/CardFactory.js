
class GoldCard {
    constructor() {
        this.type = "gold";
        this.discount = 5;
        this.color = 'gold';
    }

    display() {
        return `Type: ${this.type}, Benefits: ${this.benefits}`;
    }
}

// Клас BonusCard представляє бонусну картку
class BonusCard {
    constructor() {
        this.type = "bonus";
        this.discount = 10;
        this.color = 'black';
    }

    display() {
        return `Type: ${this.type}, Benefits: ${this.benefits}`;
    }
}

// Клас SocialCard представляє соціальну картку
class SocialCard {
    constructor() {
        this.type = "social";
        this.discount = 15;
        this.color = 'yellow';
    }

    display() {
        return `Type: ${this.type}, Benefits: ${this.benefits}`;
    }
}

// Фабрика карток
export class CardFactory {
    static createCard(cardType) {
        switch (cardType) {
            case "gold":
                return new GoldCard();
            case "bonus":
                return new BonusCard();
            case "social":
                return new SocialCard();
            default:
                return null;
        }
    }
}