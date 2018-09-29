#!/usr/bin/env bash

distribution () {
    # Setup distribution
    python setup.py sdist bdist_wheel
}

create_tag () {
    echo "Enter release version: "
    read releaseVersion

    # Pull the latest code from master branch
    git pull origin master
    # Create release tag
    git tag $releaseVersion
    # push release tag to git
    git push origin $releaseVersion
}

release () {
    cd browserium/

    # Release version to TestPyPi
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

    # Release verstion to PyPi
    twine upload dist/*
}

current_branch=$(git branch | grep \* | cut -d ' ' -f2)
#Check for current branch
if [ $current_branch = 'develop' ];
then
    # checkout to master branch at first
    git checkout master
    create_tag
    distribution
    release
elif [ $current_branch = 'master' ];
then
    create_tag
    distribution
    release
else
    echo "Not a release branch"
fi