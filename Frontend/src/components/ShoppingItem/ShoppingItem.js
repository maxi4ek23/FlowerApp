import { useState } from "react"
import { useSelector } from "react-redux"
import './ShoppingItem.css';
import { useDispatch } from "react-redux";
import {removeFromOrder, increaseCount, decreaseCount} from '../../redux/orderSlice';


const ShoppingItem = ({ id, name, price}) => {
    const items = useSelector((state) => state.order.orderItems);
    const item = items[items.findIndex((anyItem) => anyItem.item.id == id)]
    const [itemCount, setItemCount] = useState(item.count);
    const expense = price * itemCount;
    const dispatch = useDispatch();

    const pressPluss = () => {
        dispatch(increaseCount(item));
        setItemCount(itemCount+1)
    }

    const pressMinus = () => {
        if (itemCount > 1) {
            dispatch(decreaseCount(item));
            setItemCount(itemCount-1)
        }
        else {
            alert("if u want delete this item press button delete");
        }
    }

    return (
        <div className="shop__item">
            <h2 className="shop__name">{name} Bouquet</h2>
            <div className="shop__count">
                <button className="shop__btn" onClick={pressMinus}>-</button>
                <h2 className="shop__num">{itemCount}</h2>
                <button className="shop__btn" onClick={pressPluss}>+</button>
            </div>
            <h2 className="shop__num">${expense}</h2>
            <button className="delete" onClick={()=> {dispatch(removeFromOrder(item))}}>delete</button>
        </div>
    )
}

export default ShoppingItem;