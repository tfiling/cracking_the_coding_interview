package solutions_test

import (
	"go_solutions/solutions"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_merge(t *testing.T) {
	type args struct {
		nums1 []int
		m     int
		nums2 []int
		n     int
	}
	tests := []struct {
		name     string
		args     args
		expected []int
	}{
		{
			name: "Example 1",
			args: args{
				nums1: []int{1, 2, 3, 0, 0, 0},
				m:     3,
				nums2: []int{2, 5, 6},
				n:     3,
			},
			expected: []int{1, 2, 2, 3, 5, 6},
		},
		{
			name: "Example 2",
			args: args{
				nums1: []int{1},
				m:     1,
				nums2: []int{},
				n:     0,
			},
			expected: []int{1},
		},
		{
			name: "Example 3",
			args: args{
				nums1: []int{0},
				m:     0,
				nums2: []int{1},
				n:     1,
			},
			expected: []int{1},
		},
		{
			name: "All elements from nums2 are smaller",
			args: args{
				nums1: []int{4, 5, 6, 0, 0, 0},
				m:     3,
				nums2: []int{1, 2, 3},
				n:     3,
			},
			expected: []int{1, 2, 3, 4, 5, 6},
		},
		{
			name: "All elements from nums2 are larger",
			args: args{
				nums1: []int{1, 2, 3, 0, 0, 0},
				m:     3,
				nums2: []int{4, 5, 6},
				n:     3,
			},
			expected: []int{1, 2, 3, 4, 5, 6},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			solutions.Merge(tt.args.nums1, tt.args.m, tt.args.nums2, tt.args.n)
			assert.Equal(t, tt.expected, tt.args.nums1)
		})
	}
}
