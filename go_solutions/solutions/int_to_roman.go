package solutions

func intToRoman(num int) string {
	//TODO - Started in Go and moved to Python
	result := ""
	romanDigits := map[int]string{
		1:    "I",
		5:    "V",
		10:   "X",
		50:   "L",
		100:  "C",
		500:  "D",
		1000: "M",
	}
	for num > 0 {
		msDigit := getMSDigit(num)
		if msDigit == 4 {
			result += romanDigits[1] + romanDigits[5]
		} else if msDigit == 9 {
			result += romanDigits[1] + romanDigits[10]
		} else {
			result += romanDigits[msDigit]
		}

	}
	return ""
}

func getMSDigit(num int) int {
	factor := 1
	for num > 10 {
		num = num / 10
	}
	return num * (10 ^ factor)
}
