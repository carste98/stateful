# This folder contains the scripts used to verify functionality and measure metrics 

## Verify functionality
### Scripts
1. checkVersion.py - 
   Sends a request to a psql database and retrieves the version of it.
   This can be used to check that a psql is up and running and verify that it uses the correct version.


## Measure Documentation (Done 2022-05-03)

Measuring documentation is done by using the script `measureSizeOfContentInFolder.py`, `measureMD.py`, and `countWordsInFolder.py`. Every docs folder is downloaded using **subversion** or `svn`.
If the need to replicate this measurement arises, the full download of all documentation can be automated using `downloadDocs.sh`.

### Scripts
1. measureSizeOfContentInFolder.py -
   Measure total size of all files in a folder by iterating through each layer (not counting symbolic links).
2. measureMD.py -
   Measure the total size of all .md files in a folder (used a a "make-do" solution for non-centralized documentation).


### Methodology measuring documentation in bytes

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
5. Running the script for each of the folders
```
python3 ./measureSizeOfContentInFolder.py ../../docs/kopf-docs/ ../../docs/kudo-docs/ ../../docs/operator-sdk-docs/
```
where the relative path to the docs are passed as arguments
```console
kopf-docs 2320730 bytes
kudo-docs 455792 bytes
operator-sdk-docs 3348450 bytes
```
6. Due to lack of centralized documentation, another script was made to measure the documentation for **Shell Operator** called `measureMD.py` which instead of measuring the total size of a whole folder of documentation, measures the total size of all markdown (.md) files in a folder. To do this, the whole shell operator repository was downloaded and then used by the script: `python3 ./python3 ./measureMD.py ../../docs/shell-operator.git/trunk`
```console
shell-operator.git 2742108 bytes
```

### Results (bytes)
```console
kopf-docs 2320730 bytes
kudo-docs 455792 bytes
operator-sdk-docs 3348450 bytes
shell-operator-trunk 118330 bytes
```
NOTE: shell operator is measures in total size of .md files instead of docs.

### Methodology measuring documentation in word count

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
5. For shell-operator, there is a lack of centralized documentation and thus the whole github repository was simply cloned. The trunk folder is renamed to `shell-operator-trunk` to give nicer output for the script.

6. Use the script `countWordsInFolder.py` with the downloaded docs : `python3 ./countWordsInFolder.py countWordsInFolder.py ../../docs/kopf-docs/ ../../docs/kudo-docs/ ../../docs/operator-sdk-docs/ ../../docs/shell-operator.git/shell-operator-trunk/`.

```console
folder name: kopf-docs - 32814 words
folder name: kudo-docs - 19663 words
folder name: operator-sdk-docs - 67185 words
folder name: shell-operator-trunk - 9695 words
```








## Measure amount of code written to create the operator

When measuring amount of code there are several things you could factor in such as code for deploying such as dockerfiles and script, but this comparison will only take in to consideration the operator code. As the operator gets bigger, the code needed to setup the operator in your cluster will start to contribute less to the overall amount of code.

By creating a new script called `amountWrittenCode.sh` which uses the script `measureSizeOfContentInFolder.py` we can measure sizes of folders and then print the output to a `results.txt`.

By moving the code which is responsible for creating the operator in each of the frameworks to separate folders and then passing them as arguments to the script `./amountWrittenCode.sh kopf-code kudo-code operator-sdk-code/ shell-operator-code/` we get:

```txt
folder name: kopf-code - 1966 bytes
folder name: kudo-code - 1902 bytes
folder name: operator-sdk-code - 1172 bytes
folder name: shell-operator-code - 1396 bytes
```


