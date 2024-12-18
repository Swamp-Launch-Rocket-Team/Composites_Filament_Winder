# Composites_Filament_Winder

Repository for code and documentation for the filament winder.

## Getting Set Up

### Installing Git
1. Install git: https://git-scm.com/
2. Run "git --version" in your command line to verify proper installation
3. Create a new folder to store this repository
4. Run "git init" in this folder to create a local repository
5. Run "git remote add origin [remote repository URL]" to add the remote repository
6. Run "git pull origin main". You will likely have to log in to your GitHub account at this point.

For other common commands, see: https://github.com/joshnh/Git-Commands

### Installing PlatformIO
PlatformIO is an extension in VSCode for programming microcontrollers, such as Arduinos. I think it is a much more pleasant experience than the default Arduino IDE. To set up PlatformIO, follow this video: https://www.youtube.com/watch?app=desktop&v=NdgMuZBpyo8&t=0s

## Pushing Changes
To push changes, create a new branch (that will eventually be merged with main). Don't commit directly to main to avoid conflicts.
1. Run "git branch [branch name]" to create a new branch
2. Run "git checkout [branch name]" to switch to that branch

Now you can commit changes to this branch. When you are ready to push to the GitHub, do the following:
1. Run "git push -u origin [branch name]" to push to a remote version of that branch
2. On GitHub (or, there are ways to do this in your terminal), merge the two branches.

## Project Structure
Currently, the project is organized into three folders.
1. /winder_controller: Code to be run on the Arduino that controls the winder
2. /programming: Program to be used on a desktop/laptop to create a configuration file that is transferred to the Arduino. This is where we will set wind angle, plies, and other settings.
3. /documentation: Any documentation for the winder.
