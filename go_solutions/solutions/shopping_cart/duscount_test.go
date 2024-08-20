package shoppingcart

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGetFixedPriceDiscountApplyer(t *testing.T) {
	type args struct {
		productName string
		quantity    int
		newPrice    float32
	}
	tests := []struct {
		name             string
		args             args
		cart             Cart
		expectedProducts map[string]Product
	}{
		// Test cases removed
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			discountApplyer := GetFixedPriceDiscountApplyer(tt.args.productName, tt.args.quantity, tt.args.newPrice)
			discountApplyer(&tt.cart)
			if !reflect.DeepEqual(tt.cart.ProductsInCart, tt.expectedProducts) {
				t.Errorf("GetFixedPriceDiscountApplyer() = %v, want %v", tt.cart.ProductsInCart, tt.expectedProducts)
			}
		})
	}
}

func TestGetExtraFreeUnitDiscountApplyer(t *testing.T) {
	type args struct {
		productName       string
		quantity          int
		addedFreeQuantity int
	}
	tests := []struct {
		name             string
		args             args
		cart             Cart
		expectedProducts map[string]Product
	}{
		{
			name: "Simple test case",
			args: args{
				productName:       "Milk",
				quantity:          2,
				addedFreeQuantity: 1,
			},
			cart: Cart{
				ProductsInCart: map[string]Product{
					"Milk": {
						Name:     "Milk",
						Price:    21,
						Quantity: 3,
					},
				},
				ProductCatalog: map[string]Product{
					"Milk": {
						Name:  "Milk",
						Price: 7,
					},
				},
			},
			expectedProducts: map[string]Product{
				"Milk": {
					Name:     "Milk",
					Price:    14,
					Quantity: 3,
				},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			discountApplyer := GetExtraFreeUnitDiscountApplyer(tt.args.productName, tt.args.quantity, tt.args.addedFreeQuantity)
			discountApplyer(&tt.cart)
			assert.Equal(t, tt.expectedProducts, tt.cart.ProductsInCart)
		})
	}
}
