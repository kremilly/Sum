# ![Icon](https://i.imgur.com/uM98gs9.png) Sum

Checksum file cli | [Download](https://github.com/thesilvaemily/sum/releases) | By: [@thesilvaemily](https://github.com/thesilvaemily)

## Example of use

* Basic usage: ``sum -f README.md -a md5``
* Export hash: ``sum -f README.md -a md5 -e hash-exported.txt``
* Verify hash: ``sum -f README.md -a md5 -v fe91b3ef61a9680410244c26165a0c3a``

## Algorithms supported

* MD5
* CRC32
* SHA1
* SHA 224
* SHA 384
* SHA 512
* Blake2B

## Parameters

* *-f* or *--file*      File to be hashed
* *-a* or *--algo*      Algorithm to be used
* *-e* or *--export*    Export hash to file
* *-v* or *--verify*    Verify hash
