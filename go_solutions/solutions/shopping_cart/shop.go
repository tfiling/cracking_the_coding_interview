package shoppingcart

import "fmt"

const (
	milk = "Milk"
	eggs = "Eggs"
)

var shelf = map[string]Product{
	milk: {
		Name:  milk,
		Price: 7,
	},
	eggs: {
		Name:  eggs,
		Price: 12,
	},
}

// Maps product name to discounts
var discounts = map[string][]DiscountApplyer{
	eggs: {GetFixedPriceDiscountApplyer(eggs, 2, 20)},
	milk: {GetExtraFreeUnitDiscountApplyer(milk, 2, 1)},
}

func RunExample() {
	cart := &Cart{
		ProductsInCart: make(map[string]Product),
		ProductCatalog: shelf,
		Discounts:      discounts,
	}
	added := []string{milk, eggs, milk, eggs, milk, milk}
	for _, pName := range added {
		cart.AddProduct(pName)
		fmt.Println(cart.CalculateCheckoutPrice())
	}
	cart.RemoveProduct(milk)
	fmt.Println(cart.CalculateCheckoutPrice())
}
