import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    orderItems: [],
    orderTotalPrice: 0,
};

const orderSlice = createSlice({
    name: 'order',
    initialState,
    reducers: {
        addToOrder(state, action) {
            console.log(action.payload)
            const newItem = action.payload;
            const existItem = state.orderItems.find((orderItem) => orderItem.item.id == newItem.item.id);
            console.log(newItem);
            state.orderTotalPrice += newItem.item.price * newItem.count;
            if (!existItem) {
                state.orderItems.push(newItem);
            }
            else {
                existItem.count += newItem.count;
            }
        },
        removeFromOrder(state, action) {
            const deleteItem = action.payload
            const currentItems = state.orderItems.filter((orderItem) => orderItem.item.id != deleteItem.item.id);
            state.orderItems = currentItems
            state.orderTotalPrice -= deleteItem.item.price * deleteItem.count;
            console.log(state.orderTotalPrice)
        },
        increaseCount(state, action) {
            const existItem = action.payload;
            const existIndex = state.orderItems.findIndex((orderItem) => orderItem.item.id == existItem.item.id);
            state.orderItems[existIndex].count += 1;
            state.orderTotalPrice += state.orderItems[existIndex].item.price;
        },
        decreaseCount(state, action) {
            const existItem = action.payload;
            const existIndex = state.orderItems.findIndex((orderItem) => orderItem.item.id == existItem.item.id);
            state.orderItems[existIndex].count -= 1;
            state.orderTotalPrice -= state.orderItems[existIndex].item.price;
        },
        clear(state, action) {
            state.orderItems = [];
            state.orderTotalPrice = 0;
        }
    },
});

export const {addToOrder, removeFromOrder, increaseCount, decreaseCount, clear} = orderSlice.actions;
export default orderSlice.reducer;