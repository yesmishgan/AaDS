for i in {1..102};
do 
cat "tests/testsB/Input/${i}.txt" | python3 richman.py > out.txt
RESULT=$(diff out.txt tests/testsB/Output/${i}.txt)
echo "tests/testsB/Input/${i}.txt"
echo "tests/testsB/Output/${i}.txt"
if [ -z "$RESULT" ]; then
    echo "TEST ${i}: OK"
else
    echo "TEST ${i}: FAILED"
fi;
done
