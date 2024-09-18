package interesting_patterns

import (
	"fmt"
	"sync"
)

type Worker struct {
	pendingWork chan string
	wg          sync.WaitGroup
}

func NewWorker(workloadCap int) *Worker {
	w := Worker{
		pendingWork: make(chan string, workloadCap),
	}

	go func() {
		defer w.wg.Done()
		for input := range w.pendingWork {
			//Simulate work
			fmt.Printf("Processing %s\n", input)
		}
	}()
	return &w
}

func (w *Worker) Shutdown() {
	//Provide a graceful shutdown
	close(w.pendingWork)
	w.wg.Wait()
}

func (w *Worker) Process(input string) {
	select {
	case w.pendingWork <- input:
	default:
		fmt.Printf("Work queue is full, probably due to a potential error")
	}
}
