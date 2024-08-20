package solutions

import (
	"testing"

	"github.com/stretchr/testify/assert"
)
// func Test_candy(t *testing.T) {
// 	tests := []struct {
// 		name     string
// 		ratings  []int
// 		expected int
// 	}{
// 		{
// 			name:     "example 1",
// 			ratings:  []int{1, 0, 2},
// 			expected: 5,
// 		},
// 		{
// 			name:     "example 2",
// 			ratings:  []int{1, 2, 2},
// 			expected: 4,
// 		},
// 		{
// 			name:     "all children have the same rating",
// 			ratings:  []int{1, 1, 1, 1, 1},
// 			expected: 5,
// 		},
// 		{
// 			name:     "ratings in ascending order",
// 			ratings:  []int{1, 2, 3, 4, 5},
// 			expected: 15,
// 		},
// 		{
// 			name:     "ratings in descending order",
// 			ratings:  []int{5, 4, 3, 2, 1},
// 			expected: 15,
// 		},
// 		{
// 			name:     "ratings with a peak in the middle",
// 			ratings:  []int{1, 3, 5, 3, 1},
// 			expected: 9,
// 		},
// 		{
// 			name:     "ratings with a valley in the middle",
// 			ratings:  []int{5, 3, 1, 3, 5},
// 			expected: 11,
// 		},
// 		{
// 			name:     "alternating ratings",
// 			ratings:  []int{1, 3, 1, 3, 1, 3},
// 			expected: 10,
// 		},
// 		{
// 			name:     "single child",
// 			ratings:  []int{1},
// 			expected: 1,
// 		},
// 		{
// 			name:     "two children with same rating",
// 			ratings:  []int{1, 1},
// 			expected: 2,
// 		},
// 		{
// 			name:     "two children with different ratings",
// 			ratings:  []int{1, 2},
// 			expected: 3,
// 		},
// 		{
// 			name:     "ratings with multiple peaks and valleys",
// 			ratings:  []int{1, 2, 87, 87, 87, 2, 1},
// 			expected: 13,
// 		},
// 		{
// 			name:     "ratings at max constraint value",
// 			ratings:  []int{20000, 20000, 20000},
// 			expected: 3,
// 		},
// 	}

// 	for _, tt := range tests {
// 		t.Run(tt.name, func(t *testing.T) {
// 			result := candy(tt.ratings)
// 			assert.Equal(t, tt.expected, result)
// 		})
// 	}
// }


func Test_candy(t *testing.T) {
	tests := []struct {
		name string
		ratings []int
		expected int
	}{
		{
			"example 1",
			[]int{1,0,2},
			5,
		},
		{
			"example 2",
			[]int{1,2,2},
			4,
		},
		{
			name:     "all children have the same rating",
			ratings:  []int{1, 1, 1, 1, 1},
			expected: 5,
		},
		{
			name:     "ratings in ascending order",
			ratings:  []int{1, 2, 3, 4, 5},
			expected: 15,
		},
		{
			name:     "ratings in descending order",
			ratings:  []int{5, 4, 3, 2, 1},
			expected: 15,
		},
		{
			name:     "ratings with a peak in the middle",
			ratings:  []int{1, 3, 5, 3, 1},
			expected: 9,
		},
		{
			name:     "ratings with a valley in the middle",
			ratings:  []int{5, 3, 1, 3, 5},
			expected: 11,
		},
		{
			name:     "alternating ratings",
			ratings:  []int{1, 3, 1, 3, 1, 3},
			expected: 9,
		},
		{
			name:     "single child",
			ratings:  []int{1},
			expected: 1,
		},
		{
			name:     "two children with same rating",
			ratings:  []int{1, 1},
			expected: 2,
		},
		{
			name:     "two children with different ratings",
			ratings:  []int{1, 2},
			expected: 3,
		},
		{
			name:     "ratings with multiple peaks and valleys",
			ratings:  []int{1, 2, 87, 87, 87, 2, 1},
			expected: 13,
		},
		{
			name:     "ratings at max constraint value",
			ratings:  []int{20000, 20000, 20000},
			expected: 3,
		},
		{
			name:     "wrong answer 1",
			ratings:  []int{1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4},
			expected: 47,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			res := candy(tt.ratings)
			assert.Equal(t, tt.expected, res)
		})
	}
}
