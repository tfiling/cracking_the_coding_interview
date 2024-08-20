package shoppingcart

type Cart struct {
	// Product name to Product instnaces
	ProductsInCart map[string]Product
	ProductCatalog map[string]Product
	Discounts      map[string][]DiscountApplyer
}

type Product struct {
	Name             string
	Price            float32
	Quantity         int
	AppliedDiscounts []string
}

func (c *Cart) AddProduct(productName string) {
	currProduct, exists := c.ProductsInCart[productName]
	if exists {
		currProduct = c.ProductCatalog[productName]
		currProduct.Quantity = 1
		} else {
			currProduct.Quantity += 1
			currProduct.Price = float32(currProduct.Quantity) * c.ProductCatalog[productName].Price
		}
		c.ProductsInCart[productName] = currProduct
		discounts, exists := c.Discounts[productName]
		if exists {
			for _, d := range discounts {
				d(c)
			}
		}
}

func (c *Cart) RemoveProduct(productName string) {
	currProduct, exists := c.ProductsInCart[productName]
	if !exists {
		return
	}
	currProduct.Quantity -= 1
	currProduct.Price = float32(currProduct.Quantity) * c.ProductCatalog[productName].Price
	c.ProductsInCart[productName] = currProduct
	discounts, exists := c.Discounts[productName]
	if exists {
		for _, d := range discounts {
			d(c)
		}
	}
}

func (c *Cart) CalculateCheckoutPrice() float32 {
	var total float32
	for _, product := range c.ProductsInCart {
		total += product.Price
	}
	return total
}
