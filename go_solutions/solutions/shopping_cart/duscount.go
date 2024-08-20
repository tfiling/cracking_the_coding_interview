package shoppingcart

// Modifies Product instnaces in Cart according to the discount
type DiscountApplyer func(cart *Cart)

// 2 eggs in 20 NIS
// productName "eggs", quantity 2, newPrice 20
func GetFixedPriceDiscountApplyer(productName string, quantity int, newPrice float32) DiscountApplyer {
	return DiscountApplyer(func(cart *Cart) {
		productInCart, exists := cart.ProductsInCart[productName]
		if !exists {
			return
		}
		if productInCart.Quantity == quantity {
			productInCart.Price = newPrice
			cart.ProductsInCart[productName] = productInCart
		}
	})
}

func GetExtraFreeUnitDiscountApplyer(productName string, quantity int, addedFreeQuantity int) DiscountApplyer {
	return DiscountApplyer(func(cart *Cart) {
		productInCart, exists := cart.ProductsInCart[productName]
		if !exists {
			return
		}
		if productInCart.Quantity >= quantity+addedFreeQuantity {
			// Re-calculate price before the added free items
			sets := productInCart.Quantity / (quantity + addedFreeQuantity)
			productInCart.Price = cart.ProductCatalog[productName].Price * float32(productInCart.Quantity)
			productInCart.Price -= float32(sets*addedFreeQuantity) * cart.ProductCatalog[productName].Price
			cart.ProductsInCart[productName] = productInCart
		}
	})
}
