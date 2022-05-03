# This folder contains the scripts used to verify functionality, mesaure metrics and other

## Verify functionality
### Scripts
1. checkVersion.py - 
   Sends a request to a psql database and retrieves the version of it.
   This can be used to check that a psql is up and running and verify that it uses the correct version.


## Measure Documentation

Measuring documentation is done by using the script `mesaureDocumentation.py`. Every docs folder is downloaded using **subversion** or `svn`.

This is achieved by:

1. finding the github link to the docs, for example:
```
https://github.com/operator-framework/operator-sdk/tree/master/website/content/en/docs
```
2. replacing `/tree/master/` with `trunk`.
```
https://github.com/operator-framework/operator-sdk/trunk/website/content/en/docs
```
3. using **subversion** to download it into a folder.

```console
svn checkout https://github.com/operator-framework/operator-sdk/trunk/website/content/en/docs
```
4. Renaming the docs to showcase which framework the documentation is part of:
```console
mv docs operator-sdk-docs
```
5. Running the script for each of the folders:
