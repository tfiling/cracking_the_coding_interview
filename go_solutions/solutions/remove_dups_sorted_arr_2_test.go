package solutions

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_removeDuplicates(t *testing.T) {
	tests := []struct{
		name string
		args []int
		expected []int
	}{
		{
			name: "example 1",
			args: []int{1,1,1,2,2,3},
			expected: []int{1,1,2,2,3},
		},
		{
			name: "example 2",
			args: []int{0,0,1,1,1,1,2,3,3},
			expected: []int{0,0,1,1,2,3,3},
		},
		{
			name: "all unique elements",
			args: []int{1,2,3,4,5},
			expected: []int{1,2,3,4,5},
		},
		{
			name: "all elements appear twice",
			args: []int{1,1,2,2,3,3,4,4},
			expected: []int{1,1,2,2,3,3,4,4},
		},
		{
			name: "some elements appear more than twice",
			args: []int{1,1,1,2,2,2,3,3,3,4,4,4},
			expected: []int{1,1,2,2,3,3,4,4},
		},
		{
			name: "negative numbers",
			args: []int{-3,-3,-2,-1,-1,0,0,0,1,2,2},
			expected: []int{-3,-3,-2,-1,-1,0,0,1,2,2},
		},
		{
			name: "single element",
			args: []int{1},
			expected: []int{1},
		},
		{
			name: "two identical elements",
			args: []int{1,1},
			expected: []int{1,1},
		},
		{
			name: "three identical elements",
			args: []int{1,1,1},
			expected: []int{1,1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := removeDuplicates(tt.args)
			assert.Equal(t, len(tt.expected), got)
			for i := range tt.expected {
				assert.Equal(t, tt.expected[i], tt.args[i])
			}
		})
	}
}
