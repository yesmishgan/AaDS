for i in {1..15};
do 
cat "tests/testsB/input${i}.txt" | python3 main.py > out.txt
RESULT=$(diff out.txt tests/testsB/answer${i}.txt)
echo "tests/testsB/input${i}.txt"
echo "tests/testsB/answer${i}.txt"
if [ -z "$RESULT" ]; then
    echo "TEST ${i}: OK"
else
    echo "TEST ${i}: FAILED"
fi;
done
