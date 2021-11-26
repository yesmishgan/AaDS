for i in {1..1};
do 
less tests/testsD/Q/${i}.txt | python3 trie.py > out.txt
RESULT=$(diff out.txt tests/testsD/A/${i}_a.txt)
echo "tests/testsD/Q/${i}.txt"
echo "tests/testsD/A/${i}_a.txt"
if [ -z "$RESULT" ]; then
    echo "TEST ${i}: OK"
else
    echo "TEST ${i}: FAILED"
fi;
done