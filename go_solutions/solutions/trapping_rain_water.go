package solutions

import "sort"

type tuple struct {
	height int
	index int
}

func trap(height []int) int {
	waterHeight := make([]int, len(height))
	tuples := make([]tuple, len(height))
	for i := range height {
		tuples[i] = tuple{
			height: height[i],
			index: i,
		}
	}
	sort.Slice(tuples, func(i, j int) bool {
		if tuples[i].height == tuples[j].height {
			return tuples[i].index < tuples[j].index
		}
		return tuples[i].height > tuples[j].height
	})
	for i, currPeak := range tuples {
		nextStepHeight := 0
		for _, nextPeak := range tuples[i+1:] {
			if nextPeak.height < currPeak.height {
				nextStepHeight = nextPeak.height
				break
			}
		}
		for _, nextPeak := range tuples[i+1:] {
			if nextPeak.height < nextStepHeight {
				// We are no longer scanning between two peaks. Iteration for currPeak completed
				break
			}
			if waterHeight[nextPeak.index] != 0 {
				// Water height already calculated from a hogher peak
				continue
			}
			from := min(currPeak.index, nextPeak.index)
			to := max(currPeak.index, nextPeak.index)
			currWaterHeight := min(currPeak.height, nextPeak.height)
			for j := from; j <= to; j++ {
				if waterHeight[j] == 0 {
					waterHeight[j] = currWaterHeight
				}
			}
		}
	}
	waterSum := 0
	for i := range height {
		if height[i] < waterHeight[i] {
			waterSum += waterHeight[i] - height[i]
		}
	}
	return waterSum
}

func min(a, b int) int {
	if a <= b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}