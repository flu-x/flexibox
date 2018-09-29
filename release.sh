#!/usr/bin/env bash

current_branch=$(git branch | grep \* | cut -d ' ' -f2)

release () {
    echo "Enter release version: "
    read releaseVersion

    # Pull the latest code from master branch
    git pull origin master
    # Create release tag
    git tag $releaseVersion
    # push release tag to git
    got push origin $releaseVersion

}

#Check for current branch
if [ $current_branch = 'develop' ];
then
    # checkout to master branch at first
    git checkout master
    release
elif [ $current_branch = 'master' ];
then
    release
else
    echo "Not a release branch"
fi