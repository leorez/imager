package main

import (
	"fmt"
	"os"
	"image"
)

func main() {
	fname := "a.bmp"
	fimg, err := os.Open(fname)
	if(err != nil) {
		fmt.Printf("Error in %s Open : %d\n", fname, err)
		return
	}
	
	defer fimg.Close()
	img, _, err := image.Decode(fimg)

	bounds := img.Bounds()
	width := bounds.Max.X
	height := bounds.Max.Y

	fmt.Printf("Width: %d, Height: %d\n", width, height)
}
	
	
