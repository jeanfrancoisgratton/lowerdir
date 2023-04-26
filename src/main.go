/*
©2023 J.F.Gratton (jean-francois@famillegratton.net)
*/
package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	a := len(os.Args[1:])
	directory := "."

	if a != 0 {
		directory = os.Args[1]
	}

	dirfp, err := os.Open(directory)
	if err != nil {
		fmt.Printf("Error while opening the %s directory\n", directory)
		fmt.Println(err)
		os.Exit(-1)
	}
	files, err := dirfp.Readdir(0)
	if err != nil {
		fmt.Println("Error while reading files in directory: ", err)
		os.Exit(-2)
	}

	for _, file := range files {
		if !file.IsDir() {
			newname := strings.ToLower(file.Name())
			err := os.Rename(filepath.Join(directory, file.Name()), filepath.Join(directory, newname))
			if err != nil {
				fmt.Printf("%s %s:\n", Red("Cannot rename "), file.Name())
				fmt.Println(err)
			}
		}
	}
}
