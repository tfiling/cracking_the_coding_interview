package playground_test

import (
	"testing"

	"go_solutions/playground"
)

func TestPutAndGet(t *testing.T) {
	cache := playground.NewLRUCache[string, int](3)

	cache.Put("one", 1)
	cache.Put("two", 2)
	cache.Put("three", 3)

	val, ok := cache.Get("two")
	if !ok || val != 2 {
		t.Errorf("Expected Get(\"two\") to return 2, got %v", val)
	}

	val, ok = cache.Get("four")
	if ok || val != 0 {
		t.Errorf("Expected Get(\"four\") to return 0 and false, got %v and %v", val, ok)
	}
}

func TestEviction(t *testing.T) {
	cache := playground.NewLRUCache[string, int](2)

	cache.Put("one", 1)
	cache.Put("two", 2)
	cache.Put("three", 3)

	_, ok := cache.Get("one")
	if ok {
		t.Error("Expected \"one\" to be evicted")
	}

	val, ok := cache.Get("three")
	if !ok || val != 3 {
		t.Errorf("Expected Get(\"three\") to return 3, got %v", val)
	}
}

func TestUpdateExistingKey(t *testing.T) {
	cache := playground.NewLRUCache[string, int](2)

	cache.Put("one", 1)
	cache.Put("two", 2)
	cache.Put("one", 10)

	val, ok := cache.Get("one")
	if !ok || val != 10 {
		t.Errorf("Expected Get(\"one\") to return 10, got %v", val)
	}
}

func TestLRUOrder(t *testing.T) {
	cache := playground.NewLRUCache[string, int](3)

	cache.Put("one", 1)
	cache.Put("two", 2)
	cache.Put("three", 3)

	// Access "one" to move it to the front
	cache.Get("one")

	// Add a new item, which should evict "two"
	cache.Put("four", 4)

	_, ok := cache.Get("two")
	if ok {
		t.Error("Expected \"two\" to be evicted")
	}

	val, ok := cache.Get("one")
	if !ok || val != 1 {
		t.Errorf("Expected Get(\"one\") to return 1, got %v", val)
	}
}