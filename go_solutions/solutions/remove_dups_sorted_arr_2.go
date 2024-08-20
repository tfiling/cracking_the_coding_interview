package solutions

func removeDuplicates(nums []int) int {
    writeCorsor := 0
	for i := range nums {
		if writeCorsor >= 2 && nums[writeCorsor - 2] == nums[writeCorsor - 1] && nums[writeCorsor - 1] == nums[i] {
			continue
		}
		nums[writeCorsor] = nums[i]
		writeCorsor += 1
	}
	return writeCorsor
}