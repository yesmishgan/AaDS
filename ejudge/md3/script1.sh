RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
for i in {1..8};
do 
cat "tests/testsA/input/${i}.txt" | python3 backpack.py > out.txt
RESULT=$(diff out.txt tests/testsA/output/${i}.txt)
#echo "tests/testsA/input/${i}.txt"
#echo "tests/testsA/output/${i}.txt"
if [ -z "$RESULT" ]; then
    echo "${GREEN}[PASS]${NC} TEST ${i}"
else
    echo "${RED}[FAILED]${NC} TEST ${i}"
fi;
done
