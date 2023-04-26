// certificateManager : Écrit par Jean-François Gratton (jean-francois@famillegratton.net)
// src/cmd/root.go

package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
	"lowerdir/misc"
)

var version = "0.100 (2023.04.22)"

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:     "lowerdir {directory|current_directory}",
	Short:   "Renames all files in target directory in lowercase",
	Version: version,
	//Long:    `This tools allows you to manipulate your custom root CAs and all certificates signed against that rootCA.`,
}

var clCmd = &cobra.Command{
	Use:     "changelog",
	Aliases: []string{"cl"},
	Short:   "Shows changelog",
	Run: func(cmd *cobra.Command, args []string) {
		misc.Changelog()
	},
}

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		fmt.Println("Error ==>", err)
	}
}

func init() {
	rootCmd.AddCommand(clCmd)

	//rootCmd.PersistentFlags().StringVarP(&config.CertConfigFile, "config", "c", "defaultCertConfig.json", "certificate configuration file.")
}
