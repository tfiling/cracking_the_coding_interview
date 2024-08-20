package solutions

func Merge(nums1 []int, m int, nums2 []int, n int)  {
    // Initialize pointers for nums1, nums2, and the merged array
    i, j, k := m-1, n-1, m+n-1

    // Merge arrays from the end
    for j >= 0 {
        if i >= 0 && nums1[i] > nums2[j] {
            nums1[k] = nums1[i]
            i--
        } else {
            nums1[k] = nums2[j]
            j--
        }
        k--
    }
}