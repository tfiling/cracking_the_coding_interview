package solutions

import "sort"

type Tuple struct {
	rating int
	location int
}

func candy(ratings []int) int {
	candies := make([]int, len(ratings))
	tuples := make([]Tuple, len(ratings))
    for i, rating := range ratings {
		tuples[i] = Tuple{
			rating: rating,
			location: i,
		}
	}
	sort.Slice(tuples, func(i, j int) bool {
		return tuples[i].rating < tuples[j].rating
	})
	for _, tuple := range tuples {
		idxToLeft := tuple.location - 1
		if idxToLeft < 0 {
			idxToLeft = 0
		}
		idxToRight := tuple.location + 1
		if idxToRight > len(candies) - 1 {
			idxToRight = len(candies) - 1
		}
		var nearbyMax int
		var nearbyMaxLoc int
		if candies[idxToLeft] > candies[idxToRight] {
			nearbyMax = candies[idxToLeft]
			nearbyMaxLoc = idxToLeft
		} else {
			nearbyMax = candies[idxToRight]
			nearbyMaxLoc = idxToRight
		}
		if tuple.rating == ratings[nearbyMaxLoc] {
			if ratings[idxToLeft] == ratings[idxToRight] {
				// rating[tuple.rating] == rating[idxToLeft] == rating[idxToRight]
				candies[tuple.location] = 1
			} else if ratings[idxToLeft] > ratings[idxToRight] {
				// nearbyMaxLoc == idxToLeft
				candies[tuple.location] = candies[idxToRight] + 1
			} else {
				// nearbyMaxLoc == idxToRight
				candies[tuple.location] = candies[idxToLeft] + 1
			}
		} else {
			// tuple.rating > ratings[nearbyMaxLoc]
			candies[tuple.location] = nearbyMax + 1
		}
	}
	sum := 0
	for _, candy := range candies {
		sum += candy
	}
	return sum
}