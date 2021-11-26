for i in {1..18};
do 
cat "tests/testsC/input${i}.txt" | python3 minheap.py > out.txt
RESULT=$(diff out.txt tests/testsC/answer${i}.txt)
echo "tests/testsC/input${i}.txt"
echo "tests/testsC/answer${i}.txt"
if [ -z "$RESULT" ]; then
    echo "TEST ${i}: OK"
else
    echo "TEST ${i}: FAILED"
fi;
done