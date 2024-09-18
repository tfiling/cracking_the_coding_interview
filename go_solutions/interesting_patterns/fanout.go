package interesting_patterns

import "fmt"

func RunFanout() {
	workParts := 2000
	ch := make(chan string, workParts)
	resCh := make(chan string)
	for i := 0; i < workParts; i++ {
		go func() {
			input := <-ch
			fmt.Printf("Completed work %s\n", input)
			resCh <- fmt.Sprintf("Done %s", input)
		}()
	}

	for i := 0; i < workParts; i++ {
		ch <- fmt.Sprintf("work #%d", i)
	}

	for i := 0; i < workParts; i++ {
		<-resCh
	}
	fmt.Println("Done")
	close(ch)
	close(resCh)
}
