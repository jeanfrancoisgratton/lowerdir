// Copyright S 2022 Jean-Francois Gratton <jean-francois@famillegratton.net>

package cmd

import (
	"github.com/spf13/cobra"
	"lowerdir/executor"
	"os"
)

// rootCmd represents the base command when called without any subcommands

var version = "1.10.00 (2023.04.27), J.F.Gratton <jean-francois@famillegratton.net>"
var verboseMode = false

var rootCmd = &cobra.Command{
	Use:     "lowerdir [directory]",
	Version: version,
	Short:   "Batch file renaming tool to lowercase",
	Long:    "If no directory is specified, the current directory will be used.",
	Run: func(cmd *cobra.Command, args []string) {
		var target string
		if len(args) == 0 {
			target = "."
		} else {
			target = args[0]
		}
		executor.Rename(verboseMode, target)
	},
}

// Execute adds all child commands to the root command and sets flags appropriately.
// This is called by main.main(). It only needs to happen once to the rootCmd.
func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {

	rootCmd.PersistentFlags().BoolVarP(&verboseMode, "verbose", "v", false, "verbose output")
	//rootCmd.PersistentFlags().StringVarP(&helpers.HypervisorUser, "hvmuser", "u", "root", "Default hypervisor user")
}
