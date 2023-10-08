# Duble Side Print
A script to solve my double side printing issue on linux systems

> This script has its own limitaions. Designed just to solve my problem.

### Installation

```bash
pip3 install pypdf
pip3 install pycups

git clone https://github.com/omeroztrk/double_side_print 
cd double_side_print

sudo ln -s `pwd`/print.py /bin/dprint
```

### Usage

```bash
dprint <filename>
```

After printing the odd pages, to print the back side, take out the printed pages and reinsert to page tray. Then input `r` and press enter to print the even pages.
