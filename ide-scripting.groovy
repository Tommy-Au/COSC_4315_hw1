rm -rf testcase
mkdir testcase output

wget -np -nd -R 'index.html*' -P 'testcase' -r 'http://www2.cs.uh.edu/~dss/teaching/COSC4315/testcases/string-freqint/sample-testcases/'

for i in {1..9}
do
  python3 freqnumber.py "k=3;input=testcase/tc0$i.txt;output=output/tc0$i.out"
  if cmp -s "testcase/tc0$i.out" "output/tc0$i.out"; then
    echo "Test case - $i passed"
  else
    echo "Test case - $i failed"
  fi
done

for i in {10..10}
do
  python3 freqnumber.py "k=3;input=testcase/tc$i.txt;output=output/tc$i.out"
  if cmp -s "testcase/tc$i.out" "output/tc$i.out"; then
    echo "Test case - $i passed"
  else
    echo "Test case - $i failed"
  fi
done
