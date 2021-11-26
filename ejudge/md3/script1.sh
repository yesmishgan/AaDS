for i in {1..8};
do 
cat "tests/testsA/input/${i}.txt" | python3 backpack.py > out.txt
RESULT=$(diff out.txt tests/testsA/output/${i}.txt)
echo "tests/testsA/input/${i}.txt"
echo "tests/testsA/output/${i}.txt"
if [ -z "$RESULT" ]; then
    echo "TEST ${i}: OK"
else
    echo "TEST ${i}: FAILED"
fi;
done
