package solutions

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_trap(t *testing.T) {
	tests := []struct {
		name string
		height []int
		expected int
	}{
		{
			name: "example 1",
			height: []int{0,1,0,2,1,0,1,3,2,1,2,1},
			expected: 6,
		},
		{
			name: "example 2",
			height: []int{4,2,0,3,2,5},
			expected: 9,
		},
		{
			name: "single element",
			height: []int{5},
			expected: 0,
		},
		{
			name: "two elements",
			height: []int{3, 5},
			expected: 0,
		},
		{
			name: "three elements with water",
			height: []int{3, 0, 3},
			expected: 3,
		},
		{
			name: "descending heights",
			height: []int{5, 4, 3, 2, 1},
			expected: 0,
		},
		{
			name: "ascending heights",
			height: []int{1, 2, 3, 4, 5},
			expected: 0,
		},
		{
			name: "complex case",
			height: []int{5, 2, 1, 2, 1, 5},
			expected: 14,
		},
		{
			name: "failed sub case 1",
			height: []int{5,4,1,2},
			expected: 1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			res := trap(tt.height)
			assert.Equal(t, tt.expected, res)
		})
	}
}
